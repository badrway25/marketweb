"""Customer project views — Phase A.1.

Four surfaces:
- `ProjectListView` — "My projects" dashboard
- `ProjectCreateView` — derive a project from a live template
- `ProjectEditorView` — the form-based editor (server-rendered, no SPA)
- `ProjectPublishView` / `ProjectUnpublishView` — status transitions

All mutations delegate to `apps.projects.services`.
"""
from __future__ import annotations

from urllib.parse import urlencode

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView

from apps.catalog.models import WebTemplate
from apps.editor.schema import (
    DESIGN_TOKEN_FIELDS,
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

    Phase A.1b flow (D-087):
    - Anon user          → redirect to login with ?next preserving the
                           template slug so the journey resumes after
                           auth.
    - Authenticated user → get-or-create the project for this template
                           (one draft per owner/template) and drop the
                           user straight into the editor.

    The view is tolerant by design: a missing / unknown / non-editable
    slug bounces back to the public catalog with a clear message rather
    than blowing up. Customers never see a 500 from a stale button.
    """
    template_slug = (request.GET.get("template") or "").strip()

    # Anon path: bounce to branded login with ?next= preserved. We
    # intentionally build ?next manually (not Django's redirect_to_login
    # helper) because we want the same concrete slug to come back
    # after auth — the auth layer itself does not know about templates.
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

    if created:
        messages.success(
            request,
            f"Progetto '{project.name}' creato. Inizia a personalizzarlo qui sotto.",
        )
    else:
        messages.info(
            request,
            f"Bentornato su '{project.name}'. Riprendi da dove avevi lasciato.",
        )
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

    messages.success(request, f"Progetto '{project.name}' creato.")
    return redirect("projects:project_editor", uuid=project.uuid)


# ---------------------------------------------------------------------------
# Editor (GET + POST)
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
                f"dall'editor Foundation v1."
            )
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        project = self.project
        schema = get_schema(project.source_archetype) or []

        # Materialise the form values: override-if-present else baseline.
        groups = []
        for group in schema:
            group_fields = []
            for key_path, spec in group["fields"]:
                value = services.current_value_for(project, key_path)
                baseline = services.resolve_path_in_baseline(project, key_path)
                group_fields.append({
                    "key": key_path,
                    "spec": spec,
                    "value": value if value is not None else "",
                    "baseline": baseline,
                    "is_overridden": _has_override(project, key_path),
                })
            groups.append({
                "id": group["id"],
                "label": group["label"],
                "help": group.get("help", ""),
                "fields": group_fields,
            })

        tokens = project.tokens
        design_fields = []
        for field_name, spec in DESIGN_TOKEN_FIELDS.items():
            design_fields.append({
                "key": field_name,
                "spec": spec,
                "value": getattr(tokens, field_name),
            })

        ctx.update({
            "project": project,
            "groups": groups,
            "design_fields": design_fields,
            "locked_notes": LOCKED_KEYS_NOTE,
            "preview_url": project.preview_url_base,
            "recent_revisions": project.revisions.all()[:5],
        })
        return ctx

    def post(self, request, *args, **kwargs):
        project = self.project
        content_edits: dict[str, str] = {}
        token_edits: dict[str, str] = {}

        schema = get_schema(project.source_archetype) or []
        for group in schema:
            for key_path, spec in group["fields"]:
                field_name = f"content__{key_path}"
                if field_name in request.POST:
                    content_edits[key_path] = request.POST[field_name]

        for field_name in DESIGN_TOKEN_FIELDS:
            form_name = f"token__{field_name}"
            if form_name in request.POST:
                token_edits[field_name] = request.POST[form_name]

        try:
            touched_content = services.save_content_edits(
                project=project, edits=content_edits, editor=request.user,
            )
            touched_tokens = services.save_design_token_edits(
                project=project, token_edits=token_edits,
            )
        except Exception as exc:
            messages.error(request, f"Impossibile salvare: {exc}")
            return redirect("projects:project_editor", uuid=project.uuid)

        total = len(touched_content) + len(touched_tokens)
        if total:
            services.take_manual_revision(
                project=project,
                editor=request.user,
                label=f"{total} campi aggiornati",
            )
            messages.success(request, f"Salvato: {total} campi aggiornati.")
        else:
            messages.info(request, "Nessuna modifica da salvare.")
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
