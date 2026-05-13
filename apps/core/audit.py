"""T31 · signal-based audit log for sensitive models.

This module ships:

  - ``TRACKED_MODELS``: the small, intentionally short list of
    ``"<app>.<Model>"`` strings whose mutations are written to
    ``AuditLogEntry``. Out-of-scope models are silently ignored.
  - ``WATCHED_FIELDS``: per-model field allowlist. We do NOT serialize
    every field that changed — only the ones whose change is
    operationally meaningful (role toggles, tier transitions, status
    machine). Anything else is noise.
  - ``DENYLISTED_FIELDS``: field names that MUST NOT ever land in the
    audit row, even if they appear in WATCHED_FIELDS by mistake.
    Currently passwords and last_login.
  - Receivers for ``pre_save`` (snapshot the old row), ``post_save``
    (emit CREATED/UPDATED/PUBLISHED/UNPUBLISHED/ROLE_CHANGED), and
    ``post_delete`` (emit DELETED).

Scope (intentionally narrow)
----------------------------
- ``accounts.User`` — role/privilege changes (is_staff, is_superuser,
  is_active, email). Catches "promoted to admin" + "deactivated" +
  "email changed", three operationally critical events.
- ``catalog.WebTemplate`` — tier transitions (draft ↔ published_live),
  status, price. Catches "made-public" + "made-draft" + price
  rewrites, all of which have storefront visibility / revenue impact.
- ``commerce.Order`` — status machine + payment + fulfillment. Catches
  cancellations, refunds, status flips.

Out-of-scope
------------
- apps.editor models (customer-visible-only).
- apps.projects.CustomerProject (customer content, not staff governance).
- granular per-field encryption.
- retention / cleanup (operator deletes via admin UI manually if needed).
- read-access tracking (chi ha VISTO cosa) — modifies only.
- Inline operations on sub-models (e.g. WebTemplate.assets via inline
  admin). Captured indirectly because the parent's ``post_save`` still
  fires.

Actor resolution
----------------
Receivers consult ``apps.core.middleware.get_audit_context()``. When
the mutation happens inside a request the actor is the request user;
otherwise the actor is None and the entry is system-attributed.
"""
from __future__ import annotations

import functools
import logging

from django.apps import apps
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from django.db.models.signals import post_delete, post_save, pre_save


logger = logging.getLogger("marketweb.audit")


#: Models we audit. Format: "<app_label>.<ModelName>". Keep this list
#: short on purpose — noise drowns signal in any audit log.
TRACKED_MODELS: tuple[str, ...] = (
    "accounts.User",
    "catalog.WebTemplate",
    "commerce.Order",
)

#: Per-model allowlist of fields whose changes should land in the
#: ``changes`` JSON. Every other field change is ignored.
WATCHED_FIELDS: dict[str, frozenset[str]] = {
    "accounts.User": frozenset({"is_staff", "is_superuser", "is_active", "email", "username"}),
    "catalog.WebTemplate": frozenset({"tier", "status", "price"}),
    "commerce.Order": frozenset({"status", "payment_status", "fulfillment_status"}),
}

#: Fields whose values must NEVER reach an audit row, even if a
#: future edit accidentally adds them to WATCHED_FIELDS. Defense in
#: depth against accidentally logging a password hash.
DENYLISTED_FIELDS: frozenset[str] = frozenset({
    "password",
    "last_login",  # changes on every login — pure noise
    "stripe_customer_id",
    "stripe_payment_intent_id",
})


def _model_key(model_cls) -> str:
    """Return ``"app_label.ModelName"`` for a model class."""
    return f"{model_cls._meta.app_label}.{model_cls.__name__}"


def _watched(instance) -> frozenset[str] | None:
    """Return the WATCHED_FIELDS set for ``instance``'s model, or
    None if the model is not tracked."""
    key = _model_key(type(instance))
    if key not in TRACKED_MODELS:
        return None
    return WATCHED_FIELDS.get(key, frozenset())


def _serialize(value):
    """Coerce a field value to a JSON-friendly form. Decimal /
    datetime / enums become strings; bool/int/None pass through."""
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    return str(value)


# ---------------------------------------------------------------------------
# Snapshot of the pre-save state, stashed on the instance for the
# post_save receiver to diff against. Keyed by a sentinel attribute
# name so we don't pollute the model's public API.
# ---------------------------------------------------------------------------

_PRE_SAVE_SNAPSHOT_ATTR = "_t31_audit_pre_save_snapshot"


def _snapshot_pre_save(sender, instance, **kwargs):
    """Capture the on-disk row's WATCHED_FIELDS values before save.

    We re-fetch from the DB (instead of trusting ``instance``'s pre-
    save values) because the instance has the NEW values by the
    time pre_save fires — so without a fresh DB read we'd diff
    new-vs-new and never see a change.
    """
    watched = _watched(instance)
    if watched is None:
        return
    if instance.pk is None:
        # CREATE path — no previous row to snapshot.
        setattr(instance, _PRE_SAVE_SNAPSHOT_ATTR, None)
        return
    try:
        old = sender.objects.only(*watched).get(pk=instance.pk)
    except sender.DoesNotExist:
        setattr(instance, _PRE_SAVE_SNAPSHOT_ATTR, None)
        return
    snap = {f: getattr(old, f) for f in watched}
    setattr(instance, _PRE_SAVE_SNAPSHOT_ATTR, snap)


# ---------------------------------------------------------------------------
# Post-save: emit CREATED / UPDATED / PUBLISHED / UNPUBLISHED /
# ROLE_CHANGED depending on what changed.
# ---------------------------------------------------------------------------

def _resolve_action(model_key: str, snapshot, instance) -> tuple[str, dict]:
    """Pick the action label + diff dict for an UPDATE.

    Returns ``(action_label, changes_dict)``. The ``changes_dict``
    only includes WATCHED_FIELDS values whose old != new and that
    are not in DENYLISTED_FIELDS.
    """
    from apps.core.models import AuditLogEntry

    watched = WATCHED_FIELDS.get(model_key, frozenset())
    changes: dict[str, dict] = {}
    for field in watched:
        if field in DENYLISTED_FIELDS:
            continue
        old_value = snapshot.get(field) if snapshot else None
        new_value = getattr(instance, field, None)
        if old_value != new_value:
            changes[field] = {
                "old": _serialize(old_value),
                "new": _serialize(new_value),
            }

    if not changes:
        # No watched field changed — skip writing a noise entry.
        return "", {}

    # Special-case status transitions that deserve their own label.
    if model_key == "catalog.WebTemplate" and "tier" in changes:
        new_tier = changes["tier"]["new"]
        if new_tier == "published_live":
            return AuditLogEntry.Action.PUBLISHED, changes
        if new_tier == "draft":
            return AuditLogEntry.Action.UNPUBLISHED, changes

    if model_key == "accounts.User":
        if any(k in changes for k in ("is_staff", "is_superuser")):
            return AuditLogEntry.Action.ROLE_CHANGED, changes

    return AuditLogEntry.Action.UPDATED, changes


def _emit_post_save(sender, instance, created, **kwargs):
    """Write an AuditLogEntry for a tracked save. Skipped silently
    when no watched field changed (no noise on cosmetic updates)."""
    from apps.core.middleware import get_audit_context
    from apps.core.models import AuditLogEntry

    watched = _watched(instance)
    if watched is None:
        return

    ctx = get_audit_context()
    model_key = _model_key(type(instance))
    snapshot = getattr(instance, _PRE_SAVE_SNAPSHOT_ATTR, None)

    if created:
        # CREATE — emit a full snapshot of the watched fields, no diff.
        changes = {
            f: {"old": None, "new": _serialize(getattr(instance, f, None))}
            for f in watched
            if f not in DENYLISTED_FIELDS
        }
        action = AuditLogEntry.Action.CREATED
    else:
        action, changes = _resolve_action(model_key, snapshot, instance)
        if not action:
            # No watched-field change — don't write noise.
            return

    _write_entry(action, instance, changes, ctx)


def _emit_post_delete(sender, instance, **kwargs):
    """Write a DELETED audit entry for a tracked deletion."""
    from apps.core.middleware import get_audit_context
    from apps.core.models import AuditLogEntry

    if _watched(instance) is None:
        return

    ctx = get_audit_context()
    _write_entry(AuditLogEntry.Action.DELETED, instance, {}, ctx)


def _write_entry(action, instance, changes, ctx) -> None:
    """Persist a single AuditLogEntry row inline.

    We deliberately do NOT defer via ``transaction.on_commit`` —
    an audit row for an attempted-but-rolled-back change is
    operationally valuable forensically (an admin who started but
    aborted a destructive edit is still worth knowing about). The
    cost is one extra INSERT per tracked mutation; negligible vs
    the value of "we know it was attempted".
    """
    from apps.core.models import AuditLogEntry

    ct = ContentType.objects.get_for_model(type(instance))
    AuditLogEntry.objects.create(
        actor_id=ctx.actor_id,
        actor_repr=ctx.actor_repr,
        action=action,
        target_content_type=ct,
        target_object_id=str(instance.pk),
        target_repr=str(instance)[:255],
        changes=changes,
        request_ip=ctx.request_ip,
    )


# ---------------------------------------------------------------------------
# T32 · alerting on high-sensitivity audit actions
# ---------------------------------------------------------------------------
#
# The action labels in this set produce an operator-facing alert
# (log WARNING + email to AUDIT_ALERT_RECIPIENTS) every time an
# AuditLogEntry row with that action is written. Keep this set
# SMALL — alert fatigue defeats the purpose of an alert.
#
# Rationale per label:
#   - ROLE_CHANGED: someone toggled is_staff / is_superuser. This is
#     the single most consequential action on the auth surface — a
#     privilege escalation deserves to wake someone up.
#   - DELETED: a tracked object was destroyed. For User this is
#     "account vanished"; for Order it is "audit trail of a sale
#     vanished"; for WebTemplate it is "public catalog item
#     unilaterally removed". All three deserve a heads-up.
#
# Out of scope (deliberately):
#   - CREATED / UPDATED / PUBLISHED / UNPUBLISHED — too high-frequency
#     and too benign to warrant push-to-operator. They remain
#     queryable in /admin/core/auditlogentry/.

ALERT_ACTIONS: frozenset[str] = frozenset({"role_changed", "deleted"})


def _format_alert_subject(entry) -> str:
    """Short, scan-friendly subject line for the audit alert email."""
    return (
        f"[MarketWeb audit] {entry.action} · "
        f"{entry.target_content_type or 'unknown'} · {entry.target_repr or entry.target_object_id}"
    )


def _format_alert_body(entry) -> str:
    """Plain-text alert body. No secrets, no full diff dumps — the
    ``changes`` dict already went through the DENYLISTED_FIELDS
    filter at write time, so it is safe to render verbatim."""
    when = entry.timestamp.isoformat() if entry.timestamp else "(no timestamp)"
    actor = entry.actor_repr or "system"
    target_ct = entry.target_content_type or "(unknown model)"
    target = entry.target_repr or entry.target_object_id or "(unknown target)"
    changes_line = repr(entry.changes) if entry.changes else "{}"
    ip_line = entry.request_ip or "-"
    return (
        f"A sensitive audit event was recorded on MarketWeb.\n\n"
        f"  When     : {when}\n"
        f"  Actor    : {actor}\n"
        f"  Action   : {entry.action}\n"
        f"  Target   : {target_ct} · {target}\n"
        f"  Changes  : {changes_line}\n"
        f"  Client IP: {ip_line}\n\n"
        f"See /admin/core/auditlogentry/{entry.pk}/ for the full row.\n"
        f"\n"
        f"This is an automated alert from the T32 audit-alerting baseline.\n"
        f"Disable by setting AUDIT_ALERTS_ENABLED=0 (break-glass only) or\n"
        f"prune the recipients via AUDIT_ALERT_RECIPIENTS in the deploy env.\n"
    )


def _emit_alert(sender, instance, created, **kwargs):
    """T32 · alert on high-sensitivity audit actions.

    Fires for every AuditLogEntry CREATE whose ``action`` is in
    ALERT_ACTIONS. Two output channels:

      1. Logger WARNING line (always emitted when enabled). Picks up
         the prod kv formatter from ``marketweb.settings.prod`` so
         log aggregators (Loki / Datadog / CloudWatch Logs Insights)
         can parse it without a custom regex.
      2. Email to ``AUDIT_ALERT_RECIPIENTS`` (skipped silently when
         the list is empty — the dev default).

    Throttle is intentionally absent: the ALERT_ACTIONS are rare by
    nature (role change / delete on User/WebTemplate/Order is a
    governance event, not a metric). If a future deploy hits alert
    fatigue, the operator path is to tighten ALERT_ACTIONS, not to
    add a digest layer here.
    """
    # post_save fires on UPDATE too — alerts are CREATE-only because
    # AuditLogEntry is append-only by design (admin enforces this);
    # an UPDATE indicates someone is manipulating the audit table
    # directly (which is itself worth knowing but out of scope here).
    if not created:
        return
    if instance.action not in ALERT_ACTIONS:
        return
    if not getattr(settings, "AUDIT_ALERTS_ENABLED", True):
        return

    # 1. Logger — always emits when alerting is enabled.
    #
    # T34 · the ``extra={...}`` dict is propagated by sentry-sdk's
    # ``BreadcrumbHandler._extra_from_record`` into the Sentry
    # breadcrumb's ``data`` dict, giving the in-Sentry forensic
    # context structured (filterable) fields instead of a flat
    # message string. The kv formatter ignores these extra keys
    # because its format string only references the standard
    # LogRecord attributes (asctime/levelname/name/message) — so
    # the log line on stdout is unchanged.
    logger.warning(
        "audit_alert action=%s actor=%s target_ct=%s target=%s changes=%r ip=%s",
        instance.action,
        instance.actor_repr or "system",
        instance.target_content_type,
        instance.target_repr or instance.target_object_id,
        instance.changes,
        instance.request_ip or "-",
        extra={
            "audit_action": instance.action,
            "audit_actor": instance.actor_repr or "system",
            "audit_target_type": str(instance.target_content_type or ""),
            "audit_target": instance.target_repr or instance.target_object_id or "",
            "audit_changes": dict(instance.changes) if instance.changes else {},
            "audit_request_ip": instance.request_ip or "",
        },
    )

    # 2. Email — only when recipients are configured.
    recipients = list(getattr(settings, "AUDIT_ALERT_RECIPIENTS", []) or [])
    if not recipients:
        return
    try:
        send_mail(
            subject=_format_alert_subject(instance),
            message=_format_alert_body(instance),
            from_email=getattr(settings, "DEFAULT_FROM_EMAIL", None),
            recipient_list=recipients,
            fail_silently=True,
        )
    except Exception as exc:  # pragma: no cover · defensive
        logger.warning(
            "audit_alert_email_failed action=%s recipients=%s error=%s",
            instance.action, recipients, exc,
        )


# ---------------------------------------------------------------------------
# T33 · @audited decorator for explicit service-layer events
# ---------------------------------------------------------------------------
#
# Some business events do not reduce to a "field X changed on model
# Y" — e.g. ``cancel_order(order, reason="customer changed mind")``
# changes Order.status from confirmed to cancelled (caught by the
# T31 signal as a generic UPDATED entry) but the *reason* never
# enters the audit row. The semantic event "this admin cancelled
# this order for THIS reason" is lost.
#
# ``@audited`` closes that gap. Decorate a service-layer function
# with an explicit ``action`` label and a small list of kwarg names
# to capture as metadata; on successful return the decorator writes
# an extra audit row carrying the semantic event.
#
# The existing T31 signal-driven UPDATED row is STILL emitted — the
# two are complementary, not duplicates. Operators get both:
#
#   - signal row : action=updated, changes={"status": {old: "confirmed", new: "cancelled"}}
#   - explicit row: action=order_cancelled, changes={"reason": "..."}
#
# Usage
# -----
#
#     from apps.core.audit import audited
#     from apps.core.models import AuditLogEntry
#
#     @audited(
#         action=AuditLogEntry.Action.ORDER_CANCELLED,
#         target_arg="order",
#         metadata_args=("reason",),
#     )
#     def cancel_order(*, order, reason=""):
#         ...
#         return order
#
# Calling ``cancel_order(order=order, reason="customer changed mind")``
# writes an AuditLogEntry with action="order_cancelled",
# target=<order>, changes={"reason": "customer changed mind"}.
#
# Failure semantics
# -----------------
# If the wrapped function raises, the audit row is NOT written. The
# exception propagates unchanged. This is the right contract: a
# semantic event ("this order WAS cancelled") only makes sense for
# operations that completed successfully.

def audited(
    *,
    action: str,
    target_arg: str,
    metadata_args: tuple[str, ...] = (),
):
    """Decorator that emits an explicit AuditLogEntry on successful
    return of the wrapped service function.

    Parameters
    ----------
    action
        The action label to record. Should be a member of
        ``AuditLogEntry.Action`` (TextChoices value or its raw string).
    target_arg
        Name of the keyword argument whose value is the audited
        target. The value must be a saved Django model instance
        (the decorator reads ``.pk``, ``type(obj)._meta`` and
        ``str(obj)``). Positional args are not supported — every
        in-scope service in the project already uses keyword-only
        signatures, which keeps the audit contract explicit.
    metadata_args
        Tuple of additional keyword-argument names whose values are
        captured into the audit row's ``changes`` JSON. Values that
        appear in ``DENYLISTED_FIELDS`` are scrubbed defensively
        (defence in depth — none of the in-scope services pass such
        kwargs today, but a future addition can't accidentally leak
        through).
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            # Write the explicit audit row only on successful return.
            try:
                _write_explicit_entry(
                    action=str(action),
                    target=kwargs.get(target_arg),
                    metadata={
                        k: kwargs[k]
                        for k in metadata_args
                        if k in kwargs and k not in DENYLISTED_FIELDS
                    },
                )
            except Exception as exc:  # pragma: no cover · defensive
                # Audit failure must never break the underlying
                # business operation that just succeeded — log and
                # swallow.
                logger.warning(
                    "audited_decorator_write_failed action=%s error=%s",
                    action, exc,
                )
            return result
        return wrapper
    return decorator


def _write_explicit_entry(*, action: str, target, metadata: dict) -> None:
    """Persist a single AuditLogEntry for an explicit service event.

    Target must be a saved model instance. If target is None (caller
    passed a positional arg or omitted the kwarg) we log a warning
    and skip — better silent skip than 500 on the business path.
    """
    from apps.core.middleware import get_audit_context
    from apps.core.models import AuditLogEntry

    if target is None or getattr(target, "pk", None) is None:
        logger.warning(
            "audited_decorator_target_missing action=%s metadata=%r",
            action, metadata,
        )
        return

    ctx = get_audit_context()
    ct = ContentType.objects.get_for_model(type(target))
    changes = {k: _serialize(v) for k, v in metadata.items()}

    AuditLogEntry.objects.create(
        actor_id=ctx.actor_id,
        actor_repr=ctx.actor_repr,
        action=action,
        target_content_type=ct,
        target_object_id=str(target.pk),
        target_repr=str(target)[:255],
        changes=changes,
        request_ip=ctx.request_ip,
    )


# ---------------------------------------------------------------------------
# Connect / disconnect helpers, called from CoreConfig.ready().
# ---------------------------------------------------------------------------

def connect_signals() -> None:
    """Wire pre_save/post_save/post_delete for every TRACKED_MODELS,
    plus the T32 alerting receiver on AuditLogEntry itself."""
    from apps.core.models import AuditLogEntry

    for key in TRACKED_MODELS:
        try:
            model_cls = apps.get_model(key)
        except LookupError:
            # Model not yet loaded — should not happen post-ready(), but
            # we degrade gracefully rather than break the boot.
            continue
        pre_save.connect(
            _snapshot_pre_save,
            sender=model_cls,
            dispatch_uid=f"t31_audit_pre_save_{key}",
        )
        post_save.connect(
            _emit_post_save,
            sender=model_cls,
            dispatch_uid=f"t31_audit_post_save_{key}",
        )
        post_delete.connect(
            _emit_post_delete,
            sender=model_cls,
            dispatch_uid=f"t31_audit_post_delete_{key}",
        )

    # T32 · alerting on the audit log itself. Fires AFTER the row
    # has been persisted (we want to surface real, durable events,
    # not transient in-memory rows).
    post_save.connect(
        _emit_alert,
        sender=AuditLogEntry,
        dispatch_uid="t32_audit_alert",
    )
