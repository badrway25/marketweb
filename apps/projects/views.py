"""Customer project views — Phase A.2 editor UX.

Four surfaces:
- `ProjectListView` — "My projects" dashboard
- `ProjectCreateView` — derive a project from a live template
- `ProjectEditorView` — the premium editor (server-rendered shell + live JS)
- `ProjectPublishView` / `ProjectUnpublishView` — status transitions
- `project_autosave` — JSON endpoint used by the debounced live autosave

All mutations delegate to `apps.projects.services`.

Phase A.2 notification-hygiene rule (D-088): the editor GET is the
primary customer surface, so it must not accumulate Django-messages
flashes. Edits go through ``project_autosave`` which returns JSON
status and never creates a flash. Only the full-page transitions
(publish / unpublish / create from new) still emit one flash each,
which the sidebar consumes and clears.
"""
from __future__ import annotations

import json
from urllib.parse import urlencode

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from apps.catalog.models import WebTemplate
from apps.editor.schema import (
    DESIGN_TOKEN_FIELDS,
    InvalidEditableField,
    LOCKED_KEYS_NOTE,
    get_schema,
    is_supported_archetype,
)
from apps.projects import selectors, services


# ---------------------------------------------------------------------------
# List + create
# ---------------------------------------------------------------------------

class ProjectListView(LoginRequiredMixin, TemplateView):
    template_name = "projects/project_list.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["projects"] = selectors.list_projects_for_owner(self.request.user)
        ctx["editable_templates"] = list(services.iter_editable_templates())
        return ctx


def customize_start(request):
    """Public customer entry point — the "Personalizza" click lands here.

    Phase A.1b flow (D-087): anon → login, auth → get-or-create.
    """
    template_slug = (request.GET.get("template") or "").strip()

    if not request.user.is_authenticated:
        login_url = reverse("accounts:login")
        this_url = request.get_full_path()
        return redirect(f"{login_url}?{urlencode({'next': this_url})}")

    if not template_slug:
        messages.error(request, "Scegli prima un template da personalizzare.")
        return redirect("catalog:template_list")

    template = (
        WebTemplate.objects.select_related("category", "brand")
        .filter(slug=template_slug, tier=WebTemplate.Tier.PUBLISHED_LIVE)
        .first()
    )
    if template is None:
        messages.error(
            request,
            "Template non disponibile per la personalizzazione.",
        )
        return redirect("catalog:template_list")

    try:
        project, created = services.get_or_create_project_for_template(
            owner=request.user, template=template,
        )
    except services.UnsupportedTemplate as exc:
        messages.info(
            request,
            "Questo template non è ancora personalizzabile online. "
            "Stiamo aprendo l'editor archetipo per archetipo — "
            f"dettaglio: {exc}",
        )
        return redirect(
            "catalog:template_detail",
            category_slug=template.category.slug,
            slug=template.slug,
        )

    # Phase A.2 notification hygiene (D-088): we used to drop a
    # "Progetto creato" / "Bentornato" flash here. On re-click from the
    # catalog the flash stacked on top of every subsequent autosave,
    # which the user surfaced as "messages that stay and repeat". The
    # editor UI now renders a context-banner for new / returning state
    # that self-dismisses — no Django-messages accumulation.
    if created:
        request.session["editor_just_created"] = True
    return redirect("projects:project_editor", uuid=project.uuid)


@login_required
@require_POST
def project_create(request):
    template_slug = request.POST.get("template_slug", "").strip()
    if not template_slug:
        messages.error(request, "Scegli un template sorgente per creare il progetto.")
        return redirect("projects:project_list")

    template = (
        WebTemplate.objects.select_related("category", "brand")
        .filter(slug=template_slug, tier=WebTemplate.Tier.PUBLISHED_LIVE)
        .first()
    )
    if template is None:
        messages.error(request, "Template non trovato o non pubblicato.")
        return redirect("projects:project_list")

    try:
        project = services.create_project_from_template(
            owner=request.user,
            template=template,
            name=request.POST.get("name") or None,
        )
    except services.UnsupportedTemplate as exc:
        messages.error(
            request,
            f"Editor non ancora disponibile per questo template: {exc}",
        )
        return redirect("projects:project_list")

    request.session["editor_just_created"] = True
    return redirect("projects:project_editor", uuid=project.uuid)


# ---------------------------------------------------------------------------
# Editor (GET + POST snapshot)
# ---------------------------------------------------------------------------

class ProjectEditorView(LoginRequiredMixin, TemplateView):
    template_name = "projects/project_editor.html"

    def dispatch(self, request, *args, **kwargs):
        self.project = selectors.get_project_for_owner(request.user, kwargs["uuid"])
        if self.project is None:
            raise Http404("Progetto non trovato.")
        if not is_supported_archetype(self.project.source_archetype):
            raise Http404(
                f"Archetipo '{self.project.source_archetype}' non supportato "
                f"dall'editor Phase A.2."
            )
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        project = self.project
        schema = get_schema(project.source_archetype) or []

        # Materialise the form values: override-if-present else baseline.
        # Groups may expose a flat "fields" list OR a "subgroups" list of
        # {label, fields} dicts — subgroups render as sub-headed dividers
        # inside the same accordion body.
        def _materialise_fields(field_pairs):
            out = []
            for key_path, spec in field_pairs:
                value = services.current_value_for(project, key_path)
                baseline = services.resolve_path_in_baseline(project, key_path)
                out.append({
                    "key": key_path,
                    "spec": spec,
                    "value": value if value is not None else "",
                    "baseline": baseline if baseline is not None else "",
                    "is_overridden": _has_override(project, key_path),
                })
            return out

        groups = []
        for group in schema:
            subgroups_spec = group.get("subgroups")
            if subgroups_spec:
                subgroups = [
                    {"label": sg["label"], "fields": _materialise_fields(sg["fields"])}
                    for sg in subgroups_spec
                ]
                flat_fields = [f for sg in subgroups for f in sg["fields"]]
            else:
                subgroups = []
                flat_fields = _materialise_fields(group["fields"])
            groups.append({
                "id": group["id"],
                "label": group["label"],
                "help": group.get("help", ""),
                "icon": group.get("icon", "bi-layers"),
                "region": group.get("region", ""),
                "fields": flat_fields,
                "subgroups": subgroups,
            })

        tokens = project.tokens
        design_fields = []
        for field_name, spec in DESIGN_TOKEN_FIELDS.items():
            design_fields.append({
                "key": field_name,
                "spec": spec,
                "value": getattr(tokens, field_name),
            })

        # Phase A.2 session-banner: on first arrival from /start/ show a
        # one-shot welcome. The key is popped so a refresh does not
        # re-show it — this is the flash-discipline contract.
        just_created = bool(self.request.session.pop("editor_just_created", False))

        override_count = project.content_overrides.count()

        # A.2.1 micro-fix: lift the language switcher from the preview
        # top-strip into the editor sidebar. Build the list of locales
        # the template has actually authored (same honest-chrome rule
        # as the public live preview — D-068).
        from apps.catalog import template_content as _tc
        from apps.catalog import template_i18n as _ti
        available_locales = _tc.get_available_locales(project.source_template.slug)
        locale_switcher = []
        if len(available_locales) > 1:
            for code in available_locales:
                chrome = _ti.get_chrome(code)
                locale_switcher.append({
                    "code": code,
                    "badge": chrome.get("lang_badge", code.upper()),
                    "label": chrome.get("lang_label", code),
                    "is_current": code == project.locale,
                })

        ctx.update({
            "project": project,
            "groups": groups,
            "design_fields": design_fields,
            "locked_notes": LOCKED_KEYS_NOTE,
            "preview_url": project.preview_url_base,
            "baseline_preview_url": f"{project.preview_url_base}&baseline=1",
            "recent_revisions": project.revisions.all()[:5],
            "just_created": just_created,
            "override_count": override_count,
            "autosave_url": reverse(
                "projects:project_autosave", kwargs={"uuid": project.uuid}
            ),
            "snapshot_url": reverse(
                "projects:project_snapshot", kwargs={"uuid": project.uuid}
            ),
            "locale_switcher": locale_switcher,
            "current_locale": project.locale,
        })
        return ctx

    # POST on the editor is intentionally a no-op in A.2 — all writes go
    # through the JSON autosave / snapshot endpoints. If a browser
    # somehow submits the legacy form, we treat it as a snapshot request
    # so no edits are lost.
    def post(self, request, *args, **kwargs):
        return project_snapshot(request, uuid=self.project.uuid)


# ---------------------------------------------------------------------------
# JSON autosave — the heart of the A.2 live-preview contract
# ---------------------------------------------------------------------------

@login_required
@require_POST
def project_autosave(request, uuid):
    """Persist a debounced batch of edits without creating a revision.

    The browser-side editor sends one POST per debounce window (~400ms)
    with only the fields that changed since the last successful save.
    This keeps the network chatter minimal and the overrides table
    sparse.

    Request body (JSON)::

        {
            "content": { "home.headline": "Nuovo titolo", ... },
            "tokens":  { "palette_primary": "#123456", ... }
        }

    Response (JSON)::

        { "ok": true, "touched": N, "override_count": M, "ts": 1713... }
        { "ok": false, "error": "..." }        (400)

    A revision is NOT taken here — autosaves are "draft writes". The
    user explicitly creates a revision via the Save button, which hits
    ``project_snapshot`` instead.
    """
    project = selectors.get_project_for_owner(request.user, uuid)
    if project is None:
        raise Http404()
    if not is_supported_archetype(project.source_archetype):
        raise Http404()

    try:
        payload = json.loads(request.body.decode("utf-8") or "{}")
    except ValueError:
        return HttpResponseBadRequest("Invalid JSON payload.")

    content_edits = payload.get("content") or {}
    token_edits = payload.get("tokens") or {}

    if not isinstance(content_edits, dict) or not isinstance(token_edits, dict):
        return HttpResponseBadRequest("content / tokens must be JSON objects.")

    try:
        touched_content = services.save_content_edits(
            project=project, edits=content_edits, editor=request.user,
        )
        touched_tokens = services.save_design_token_edits(
            project=project, token_edits=token_edits,
        )
    except InvalidEditableField as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)
    except Exception as exc:  # defensive — never 500 on a typing stroke
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)

    from django.utils import timezone

    from apps.projects.models import ProjectContent

    # Bypass the prefetch cache on `project.content_overrides` — it was
    # populated by the selector before the save and would return the
    # stale (pre-save) count.
    fresh_count = ProjectContent.objects.filter(project=project).count()

    return JsonResponse({
        "ok": True,
        "touched": len(touched_content) + len(touched_tokens),
        "content_keys": list(touched_content),
        "token_keys": list(touched_tokens),
        "override_count": fresh_count,
        "ts": int(timezone.now().timestamp() * 1000),
    })


@login_required
@require_POST
def project_snapshot(request, uuid):
    """Create a manual revision snapshot (user clicked "Salva versione")."""
    project = selectors.get_project_for_owner(request.user, uuid)
    if project is None:
        raise Http404()
    services.take_manual_revision(
        project=project,
        editor=request.user,
        label=request.POST.get("label") or "Salvataggio manuale",
    )
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse({
            "ok": True,
            "revision_count": project.revisions.count(),
        })
    messages.success(request, "Versione salvata nella cronologia.")
    return redirect("projects:project_editor", uuid=project.uuid)


@login_required
@require_POST
def project_publish(request, uuid):
    project = selectors.get_project_for_owner(request.user, uuid)
    if project is None:
        raise Http404()
    services.publish_project(project=project, editor=request.user)
    messages.success(request, "Progetto pubblicato.")
    return redirect("projects:project_editor", uuid=project.uuid)


@login_required
@require_POST
def project_unpublish(request, uuid):
    project = selectors.get_project_for_owner(request.user, uuid)
    if project is None:
        raise Http404()
    services.unpublish_project(project=project, editor=request.user)
    messages.success(request, "Progetto riportato in bozza.")
    return redirect("projects:project_editor", uuid=project.uuid)


def _has_override(project, key_path: str) -> bool:
    return any(row.key_path == key_path for row in project.content_overrides.all())
