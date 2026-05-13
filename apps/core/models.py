from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.text import slugify


class TimestampedModel(models.Model):
    """Abstract base model with created/updated timestamps."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugModel(models.Model):
    """Abstract base model with auto-generated slug from a `name` field."""

    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class AuditLogEntry(models.Model):
    """T31 · cross-cutting audit record for sensitive admin actions.

    Complements ``django.contrib.admin.models.LogEntry`` (which only
    captures admin-site interactions) by also tracking programmatic
    changes (services-layer, management commands, signal-driven
    side effects) on the small set of sensitive models declared in
    ``apps.core.audit.TRACKED_MODELS``.

    Authorship is captured via a thread-local pushed by
    ``apps.core.middleware.AuditContextMiddleware`` — when the change
    happens inside a request cycle the actor is the request user;
    when it happens outside (management command, Celery task, shell)
    the actor is None and the entry is tagged as "system".

    The ``changes`` JSONField stores a small dict of changed fields
    keyed by field name → {old, new}. Fields listed in
    ``apps.core.audit.DENYLISTED_FIELDS`` (e.g. ``password``,
    ``last_login`` noise) are NEVER serialized — neither old nor new
    value reaches the audit row.

    This model is intentionally additive (no ON DELETE CASCADE on
    target object: the audit row survives the object it describes).
    Schema is denormalized for read-side simplicity — operators
    investigating an incident need to grep one table, not JOIN three.
    """

    class Action(models.TextChoices):
        # Signal-driven labels (T31) · written automatically by the
        # post_save / post_delete receivers in apps.core.audit.
        CREATED = "created", "Created"
        UPDATED = "updated", "Updated"
        DELETED = "deleted", "Deleted"
        # Special-case status transitions that deserve a distinct
        # action label so dashboards can filter for "publish events"
        # or "role escalations" without parsing the changes dict.
        PUBLISHED = "published", "Published"  # WebTemplate.tier → published_live
        UNPUBLISHED = "unpublished", "Unpublished"  # WebTemplate.tier → draft
        ROLE_CHANGED = "role_changed", "Role changed"  # User.is_staff/is_superuser toggled
        # Explicit service-layer labels (T33) · written by the
        # ``@audited(action=...)`` decorator on selected service
        # functions. They carry semantic context (cancel reason,
        # payment note) that the signal-driven UPDATED row would
        # otherwise lose. The signal-driven UPDATED row is still
        # emitted alongside — the two are complementary, not
        # duplicates.
        ORDER_CANCELLED = "order_cancelled", "Order cancelled"
        ORDER_PAID = "order_paid", "Order paid"
        # T35 · extension of the T33 explicit-event set to three
        # additional governance-relevant flows. Same decorator,
        # same complementary-with-signal pattern for tracked targets
        # (Order), audit-only-via-explicit for untracked targets
        # (CustomerProject — not in TRACKED_MODELS so otherwise
        # invisible to the audit feed).
        ORDER_FULFILLMENT_CHANGED = "order_fulfillment_changed", "Order fulfillment changed"
        PROJECT_PUBLISHED = "project_published", "Project published"
        PROJECT_UNPUBLISHED = "project_unpublished", "Project unpublished"

    # When the change happened. Indexed for the most common admin
    # query (recent entries first).
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)

    # Who did it. NULL for system actions (management commands,
    # async tasks, signals outside a request). On user deletion the
    # audit entry survives — we keep the entry's representation in
    # ``actor_repr`` so it stays informative.
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    # Snapshot of ``str(actor)`` at the time of the action; survives
    # the actor's later username rename or account deletion.
    actor_repr = models.CharField(max_length=255, blank=True)

    # Which action. The TextChoices enum keeps the column small and
    # admin filter UI clean. ``max_length=32`` accommodates the
    # longest current label (``order_fulfillment_changed``, 25
    # chars from T35) plus a small forward-buffer for future
    # labels — keep this in sync with the longest member of
    # ``AuditLogEntry.Action``.
    action = models.CharField(
        max_length=32,
        choices=Action.choices,
        db_index=True,
    )

    # Target object · GenericForeignKey so we can audit any tracked
    # model without per-target FK columns. ``target_repr`` snapshots
    # ``str(obj)`` so deleted-target entries stay readable.
    target_content_type = models.ForeignKey(
        ContentType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    # CharField (not IntegerField) so we support UUID-keyed targets
    # alongside integer-PK ones. Indexed because investigations
    # typically start from a known PK.
    target_object_id = models.CharField(max_length=64, blank=True, db_index=True)
    target = GenericForeignKey("target_content_type", "target_object_id")
    target_repr = models.CharField(max_length=255, blank=True)

    # Small field-level diff. Shape:
    #   {"is_staff": {"old": false, "new": true}, ...}
    # Denylisted field names (passwords, last_login noise) NEVER
    # appear here — see apps.core.audit.DENYLISTED_FIELDS.
    changes = models.JSONField(default=dict, blank=True)

    # Optional request-side metadata. NULL when the change happens
    # outside a request cycle (management command, async task).
    request_ip = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ("-timestamp",)
        verbose_name = "audit log entry"
        verbose_name_plural = "audit log entries"
        indexes = [
            models.Index(fields=["target_content_type", "target_object_id"]),
            models.Index(fields=["actor", "-timestamp"]),
            models.Index(fields=["action", "-timestamp"]),
        ]

    def __str__(self):
        who = self.actor_repr or "system"
        return f"{who} · {self.action} · {self.target_repr}"
