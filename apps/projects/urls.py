from django.urls import path

from apps.projects import views

app_name = "projects"

urlpatterns = [
    path("", views.ProjectListView.as_view(), name="project_list"),
    # Public customer entry (D-087) — "Personalizza" on the catalog
    # lands on this URL.
    path("start/", views.customize_start, name="customize_start"),
    path("new/", views.project_create, name="project_create"),
    path("<uuid:uuid>/editor/", views.ProjectEditorView.as_view(), name="project_editor"),
    path("<uuid:uuid>/autosave/", views.project_autosave, name="project_autosave"),
    path("<uuid:uuid>/snapshot/", views.project_snapshot, name="project_snapshot"),
    # A.3a — repeater row ops (add / remove on mutable lists only).
    path("<uuid:uuid>/row/add/", views.project_row_add, name="project_row_add"),
    path("<uuid:uuid>/row/remove/", views.project_row_remove, name="project_row_remove"),
    # A.3b — reorder row (up/down one step).
    path("<uuid:uuid>/row/move/", views.project_row_move, name="project_row_move"),
    # A.4 — customer image upload.
    path("<uuid:uuid>/assets/upload/", views.project_asset_upload, name="project_asset_upload"),
    path("<uuid:uuid>/publish/", views.project_publish, name="project_publish"),
    path("<uuid:uuid>/unpublish/", views.project_unpublish, name="project_unpublish"),
]
