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
    is_supported_archetype,
    is_translatable,
    iter_groups,
    supported_locales,
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
        archetype = project.source_archetype

        # A.7 Step 2 — resolve the active editing locale. Reads `?lang=`
        # from the editor URL; falls back to ``project.locale`` silently
        # if the value is absent or not enrolled for the archetype.
        supported = supported_locales(archetype)
        raw_locale = self.request.GET.get("lang") or ""
        if supported and raw_locale in supported:
            active_locale = raw_locale
        else:
            active_locale = project.locale
        # A.2.6b: iter_groups returns curated + synthetic indexed-row
        # groups so the sidebar surfaces all 32 accordions for the
        # agency-creative-studio archetype (was 14 in A.2.6a).
        # A.3a: pass meta_by_path so mutable lists surface their
        # effective (post-add/remove) row list in the sidebar.
        from apps.editor.schema import STRUCTURED_FIELD_SHAPES
        meta_by_path: dict[str, dict] = {}
        for list_path, shape in (STRUCTURED_FIELD_SHAPES.get(archetype) or {}).items():
            if shape.get("mutable"):
                meta_by_path[list_path] = services.get_list_meta(project, list_path)
        schema = iter_groups(archetype, meta_by_path=meta_by_path)

        # Materialise the form values: override-if-present else baseline.
        # Groups may expose a flat "fields" list OR a "subgroups" list of
        # {label, fields} dicts — subgroups render as sub-headed dividers
        # inside the same accordion body.
        # A.7 Step 2: translatable fields read/prefill from the active
        # locale's buffer + authored registry. Global fields still read
        # plain rows + project.locale baseline.
        def _materialise_fields(field_pairs):
            out = []
            for key_path, spec in field_pairs:
                field_locale = active_locale if is_translatable(archetype, key_path) else None
                value = services.current_value_for(project, key_path, locale=field_locale)
                baseline = services.resolve_path_in_baseline(project, key_path, locale=field_locale)
                out.append({
                    "key": key_path,
                    "spec": spec,
                    "value": value if value is not None else "",
                    "baseline": baseline if baseline is not None else "",
                    "is_overridden": _has_override(project, key_path, locale=field_locale),
                    # A.7 Step 2 — UI marker: which fields are locale-scoped.
                    "translatable": is_translatable(archetype, key_path),
                })
            return out

        groups = []
        for group in schema:
            subgroups_spec = group.get("subgroups")
            if subgroups_spec:
                subgroups = [
                    {
                        "label": sg["label"],
                        "fields": _materialise_fields(sg["fields"]),
                        # A.3a — surface the row identity so template can
                        # render a targeted remove button per row.
                        "row_identity": sg.get("row_identity"),
                    }
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
                # A.2.5: page-aware targeting. ``"*"`` = chrome (nav/foot)
                # visible on every page → editor JS treats as "stay".
                "page": group.get("page", "*"),
                # A.2.5 palette search — surfaced only in the JSON index.
                "keywords": list(group.get("keywords") or []),
                "fields": flat_fields,
                "subgroups": subgroups,
                # A.3a — repeater affordances.
                "mutable": bool(group.get("mutable")),
                "min_rows": group.get("min_rows"),
                "max_rows": group.get("max_rows"),
                "list_path": group.get("list_path"),
                "effective_length": group.get("effective_length"),
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
        # A.7 Step 2 — ``is_current`` now tracks the URL-resolved
        # ``active_locale`` (not the project's seed locale) so clicking
        # a pill and reloading surfaces the right "selected" state.
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
                    "is_current": code == active_locale,
                })

        # A.2.5 page-aware targeting — the editor JS builds per-page
        # preview URLs client-side, so it needs the raw base path plus
        # the list of authored page slugs. The home URL stays available
        # as ``preview_url`` for the initial iframe src + backward-compat.
        # A.7 Step 2 — palette page labels resolve from the active
        # locale so breadcrumbs read the translated label.
        baseline_content = (
            _tc.get_content(project.source_template.slug, active_locale)
            or _tc.get_content(project.source_template.slug, project.locale)
            or {}
        )
        available_pages = [p["slug"] for p in baseline_content.get("pages", [])]

        # Page slug → display label (used by the palette breadcrumbs so
        # results read "Home · Hero · Headline" instead of "home · hero").
        # Chrome gets "Ovunque" — fields on every page.
        page_labels: dict[str, str] = {"*": "Ovunque"}
        for p in baseline_content.get("pages", []):
            page_labels[p["slug"]] = p.get("label") or p["slug"].title()

        # A.2.5 palette-search index — a flat, pre-normalised list of
        # every editable field (content + design tokens) with enough
        # context for client-side ranking. The JS parses this JSON at
        # init and never re-queries the server for search.
        palette_index = _build_palette_index(groups, design_fields, page_labels)
        # `</script>` in any label would break out of the inline <script>
        # block; neutralise defensively so we don't rely on field authors.
        palette_index_json = (
            json.dumps(palette_index, ensure_ascii=False)
            .replace("</", "<\\/")
        )

        # A.7 Step 2 — preview URL now carries ?lang=<active_locale> so
        # the iframe router picks the matching authored registry and the
        # overlay applies the per-locale rows only.
        preview_url = project.preview_url_for_page("home", locale=active_locale)
        baseline_preview_url = f"{preview_url}&baseline=1"

        ctx.update({
            "project": project,
            "groups": groups,
            "design_fields": design_fields,
            "locked_notes": LOCKED_KEYS_NOTE,
            "preview_url": preview_url,
            "baseline_preview_url": baseline_preview_url,
            "preview_base_path": project.preview_url_path,
            "available_pages": available_pages,
            "palette_index_json": palette_index_json,
            "recent_revisions": project.revisions.all()[:5],
            "just_created": just_created,
            "override_count": override_count,
            "autosave_url": reverse(
                "projects:project_autosave", kwargs={"uuid": project.uuid}
            ),
            "snapshot_url": reverse(
                "projects:project_snapshot", kwargs={"uuid": project.uuid}
            ),
            # A.3a — repeater endpoints.
            "row_add_url": reverse(
                "projects:project_row_add", kwargs={"uuid": project.uuid}
            ),
            "row_remove_url": reverse(
                "projects:project_row_remove", kwargs={"uuid": project.uuid}
            ),
            "row_move_url": reverse(
                "projects:project_row_move", kwargs={"uuid": project.uuid}
            ),
            # A.4 — customer image upload endpoint.
            "asset_upload_url": reverse(
                "projects:project_asset_upload", kwargs={"uuid": project.uuid}
            ),
            "locale_switcher": locale_switcher,
            "current_locale": active_locale,
            # A.7 Step 2 — editor_ctx contract for multi-locale editing.
            "active_locale": active_locale,
            "supported_locales": supported,
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
    # A.7 Step 2: the autosave JSON now carries an optional ``locale``
    # string. Translatable fields in ``content_edits`` land under the
    # ``@<locale>:<path>`` storage shape so edits in one language never
    # dirty another. A missing or empty locale defaults to
    # ``project.locale`` at the service layer (backward-compat).
    raw_locale = payload.get("locale")
    autosave_locale = raw_locale if isinstance(raw_locale, str) and raw_locale else None

    if not isinstance(content_edits, dict) or not isinstance(token_edits, dict):
        return HttpResponseBadRequest("content / tokens must be JSON objects.")

    try:
        touched_content = services.save_content_edits(
            project=project, edits=content_edits, editor=request.user,
            locale=autosave_locale,
        )
        touched_tokens = services.save_design_token_edits(
            project=project, token_edits=token_edits,
        )
    except InvalidEditableField as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)
    except services.UnsupportedLocale as exc:
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
def project_row_add(request, uuid):
    """A.3a — append a new row to a mutable list.

    Request body JSON: ``{"list_path": "studio.partners"}``.

    Success (200)::
        {"ok": true, "uid": "a3", "effective_length": 4,
         "override_count": 7, "jump_key": "studio.partners.a3.name"}

    Errors:
    - 400 on malformed payload or unknown/non-mutable list
    - 404 on ownership mismatch / unsupported archetype
    - 409 when max_rows guard would be crossed
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
    list_path = payload.get("list_path")
    if not isinstance(list_path, str) or not list_path:
        return HttpResponseBadRequest("list_path is required.")

    try:
        result = services.add_row(
            project=project, list_path=list_path, editor=request.user,
        )
    except services.UnsupportedMutation as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)
    except services.RowLimitReached as exc:
        return JsonResponse(
            {"ok": False, "error": str(exc), "limit_kind": exc.kind, "limit": exc.limit},
            status=409,
        )
    except Exception as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)

    from apps.projects.models import ProjectContent
    override_count = ProjectContent.objects.filter(project=project).count()
    # Suggest the sidebar field the browser should jump to after the add:
    # the first editable column of the new row, for a content-ready focus.
    from apps.editor.schema import get_list_shape
    shape = get_list_shape(project.source_archetype, list_path)
    kind = shape.get("kind")
    if kind == "scalar":
        jump_key = f"{list_path}.{result['uid']}"
    else:
        cols = shape.get("cols") or []
        first_col = cols[0][0] if cols else ""
        jump_key = f"{list_path}.{result['uid']}.{first_col}" if first_col else ""

    return JsonResponse({
        "ok": True,
        "uid": result["uid"],
        "effective_length": result["effective_length"],
        "override_count": override_count,
        "jump_key": jump_key,
    })


@login_required
@require_POST
def project_row_remove(request, uuid):
    """A.3a — remove a row from a mutable list.

    Request body JSON: ``{"list_path": "studio.partners", "index": 1}``
    OR ``{"list_path": "studio.partners", "uid": "a0"}``. Exactly one
    of ``index`` / ``uid`` must be provided.
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
    list_path = payload.get("list_path")
    index = payload.get("index")
    uid = payload.get("uid")
    if not isinstance(list_path, str) or not list_path:
        return HttpResponseBadRequest("list_path is required.")
    if (index is None) == (uid is None):
        return HttpResponseBadRequest("Provide exactly one of index / uid.")

    try:
        result = services.remove_row(
            project=project, list_path=list_path,
            index=index if uid is None else None,
            uid=uid if index is None else None,
            editor=request.user,
        )
    except services.UnsupportedMutation as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)
    except services.RowLimitReached as exc:
        return JsonResponse(
            {"ok": False, "error": str(exc), "limit_kind": exc.kind, "limit": exc.limit},
            status=409,
        )
    except InvalidEditableField as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)
    except Exception as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)

    from apps.projects.models import ProjectContent
    override_count = ProjectContent.objects.filter(project=project).count()
    return JsonResponse({
        "ok": True,
        "effective_length": result["effective_length"],
        "override_count": override_count,
    })


@login_required
@require_POST
def project_row_move(request, uuid):
    """A.3b — reorder a row one position up or down.

    Request body JSON::
        {"list_path": "studio.partners", "segment": "a0", "direction": "up"}

    Success (200): ``{"ok": true, "effective_length": N, "override_count": M}``
    Errors:
    - 400 on malformed payload / unknown list / non-mutable list /
      bad direction / missing segment
    - 404 on ownership mismatch
    - 409 when the move would cross the first/last boundary
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
    list_path = payload.get("list_path")
    segment = payload.get("segment")
    direction = payload.get("direction")
    if not isinstance(list_path, str) or not list_path:
        return HttpResponseBadRequest("list_path is required.")
    if not isinstance(segment, str) or not segment:
        return HttpResponseBadRequest("segment is required.")
    if direction not in ("up", "down"):
        return HttpResponseBadRequest("direction must be 'up' or 'down'.")

    try:
        result = services.move_row(
            project=project, list_path=list_path,
            segment=segment, direction=direction, editor=request.user,
        )
    except services.UnsupportedMutation as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)
    except services.RowLimitReached as exc:
        return JsonResponse(
            {"ok": False, "error": str(exc), "limit_kind": exc.kind, "limit": exc.limit},
            status=409,
        )
    except InvalidEditableField as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)
    except Exception as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)

    from apps.projects.models import ProjectContent
    override_count = ProjectContent.objects.filter(project=project).count()
    return JsonResponse({
        "ok": True,
        "effective_length": result["effective_length"],
        "override_count": override_count,
    })


@login_required
@require_POST
def project_asset_upload(request, uuid):
    """A.4 — customer-facing image upload.

    Request: ``multipart/form-data`` with a single ``file`` part.
    Server-side guards: 2MB size cap, MIME whitelist (jpg/png/webp),
    Pillow.verify() sanity check, ownership via project uuid.

    Success (200)::
        {"ok": true, "asset_id": 42, "url": "/media/project-assets/...",
         "size_bytes": 184523, "content_type": "image/png"}

    Errors:
    - 400 on missing file / invalid image
    - 404 on ownership mismatch
    - 413 when size > 2MB
    - 415 on disallowed MIME
    """
    project = selectors.get_project_for_owner(request.user, uuid)
    if project is None:
        raise Http404()
    if not is_supported_archetype(project.source_archetype):
        raise Http404()

    uploaded = request.FILES.get("file")
    if uploaded is None:
        return HttpResponseBadRequest("file is required.")

    try:
        asset = services.upload_asset(
            project=project, uploaded_file=uploaded, editor=request.user,
        )
    except services.AssetTooLarge as exc:
        return JsonResponse(
            {"ok": False, "error": str(exc),
             "size_bytes": exc.size_bytes, "limit_bytes": exc.limit_bytes},
            status=413,
        )
    except services.AssetMimeRejected as exc:
        return JsonResponse(
            {"ok": False, "error": str(exc), "content_type": exc.content_type},
            status=415,
        )
    except services.AssetInvalid as exc:
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)
    except Exception as exc:  # defensive — never 500 on a bad upload
        return JsonResponse({"ok": False, "error": str(exc)}, status=400)

    return JsonResponse({
        "ok": True,
        "asset_id": asset.id,
        "url": asset.file.url,
        "size_bytes": asset.size_bytes,
        "content_type": asset.content_type,
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


def _has_override(project, key_path: str, locale: str | None = None) -> bool:
    """Did the customer override this path?

    A.7 Step 2: translatable paths check for a ``@<locale>:`` row first,
    then fall back to a legacy plain row (pre-A.7 projects). Global paths
    check the plain key only. The ``locale`` kwarg is ignored for paths
    that are not translatable so the caller never has to branch.
    """
    rows = list(project.content_overrides.all())
    if locale:
        locale_key = f"@{locale}:{key_path}"
        if any(r.key_path == locale_key for r in rows):
            return True
    return any(r.key_path == key_path for r in rows)


# ---------------------------------------------------------------------------
# A.2.5 · palette-search index builder
# ---------------------------------------------------------------------------

# Icons shown next to each result row — by widget type, not by group.
_PALETTE_TYPE_ICONS = {
    "text":     "bi-type",
    "textarea": "bi-text-paragraph",
    "richtext": "bi-quote",
    "select":   "bi-chevron-contract",
    "color":    "bi-palette",
    "url":      "bi-link-45deg",
    "image":    "bi-image",
}
_PALETTE_TYPE_LABELS = {
    "text":     "Testo",
    "textarea": "Area",
    "richtext": "Rich text",
    "select":   "Select",
    "color":    "Colore",
    "url":      "URL",
    "image":    "Immagine",
}


def _build_palette_index(groups, design_fields, page_labels):
    """Flat, UI-ready index of every editable field for the palette.

    One dict per field. Shape is stable client-side; new fields never
    need server-side scoring changes. Keep the payload tiny: the JSON
    is parsed at init and lives in memory for the session, so labels
    stay short and `keywords` stays group-level.
    """
    rows = []

    for group in groups:
        group_id     = group["id"]
        group_label  = group["label"]
        group_page   = group.get("page", "*")
        group_page_l = page_labels.get(group_page, group_page)
        group_kws    = list(group.get("keywords") or [])

        def _append(field, subgroup_label=""):
            spec = field["spec"]
            ftype = spec.get("type", "text")
            rows.append({
                "key":           field["key"],
                "kind":          "content",
                "label":         spec.get("label", field["key"]),
                "help":          spec.get("help", ""),
                "placeholder":   spec.get("placeholder", ""),
                "type":          ftype,
                "type_label":    _PALETTE_TYPE_LABELS.get(ftype, ftype),
                "icon":          _PALETTE_TYPE_ICONS.get(ftype, "bi-input-cursor"),
                "group_id":      group_id,
                "group_label":   group_label,
                "subgroup_label": subgroup_label,
                "page":          group_page,
                "page_label":    group_page_l,
                "keywords":      group_kws,
            })

        if group.get("subgroups"):
            for sub in group["subgroups"]:
                for f in sub["fields"]:
                    _append(f, sub["label"])
        else:
            for f in group["fields"]:
                _append(f, "")

    # Design tokens — one virtual "group" surfaced in the palette so
    # customers can type "colori", "font", "palette" and jump to the
    # right control.
    for f in design_fields:
        spec = f["spec"]
        ftype = spec.get("type", "text")
        rows.append({
            "key":           f["key"],
            "kind":          "token",
            "label":         spec.get("label", f["key"]),
            "help":          spec.get("help", ""),
            "placeholder":   "",
            "type":          ftype,
            "type_label":    _PALETTE_TYPE_LABELS.get(ftype, ftype),
            "icon":          _PALETTE_TYPE_ICONS.get(ftype, "bi-sliders"),
            "group_id":      "design",
            "group_label":   "Colori e tipografia",
            "subgroup_label": "",
            "page":          "*",
            "page_label":    "Ovunque",
            "keywords":      ["colori", "color", "palette", "font", "tipografia", "typography", "brand", "tema"],
        })

    return rows
