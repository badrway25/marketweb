"""Read-path selectors for customer projects."""
from __future__ import annotations

import uuid as uuid_lib

from django.db.models import Prefetch

from apps.projects.models import CustomerProject, ProjectContent


def list_projects_for_owner(owner) -> list[CustomerProject]:
    """All projects owned by a user, newest first."""
    return list(
        CustomerProject.objects.filter(owner=owner)
        .select_related("source_template", "source_template__brand", "tokens")
        .order_by("-updated_at")
    )


def get_project_for_owner(owner, project_uuid: str | uuid_lib.UUID) -> CustomerProject | None:
    """Fetch a project only if it belongs to `owner`. Returns None otherwise."""
    if not _is_valid_uuid(project_uuid):
        return None
    return (
        CustomerProject.objects
        .filter(owner=owner, uuid=project_uuid)
        .select_related("source_template", "source_template__brand", "tokens")
        .prefetch_related(Prefetch("content_overrides", queryset=ProjectContent.objects.all()))
        .first()
    )


def get_project_for_preview(
    project_uuid: str | uuid_lib.UUID,
    user,
    template_slug: str,
) -> CustomerProject | None:
    """Resolve a project for a preview request.

    Foundation v1 rules:
    - Draft projects are visible only to the owner (and staff).
    - Published projects are visible to the owner + any authenticated
      user (Phase B will gate them behind share tokens).
    - The project's source template must match the URL's template slug
      to prevent arbitrary cross-template overlay.
    """
    if not _is_valid_uuid(project_uuid):
        return None
    project = (
        CustomerProject.objects
        .filter(uuid=project_uuid)
        .select_related("source_template", "tokens")
        .prefetch_related("content_overrides")
        .first()
    )
    if project is None:
        return None
    if project.source_template.slug != template_slug:
        return None
    if project.status == CustomerProject.Status.DRAFT:
        if not (user.is_authenticated and (user.is_staff or project.owner_id == user.id)):
            return None
    return project


def _is_valid_uuid(value) -> bool:
    try:
        uuid_lib.UUID(str(value))
        return True
    except (ValueError, AttributeError, TypeError):
        return False
