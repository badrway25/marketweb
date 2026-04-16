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
    path("<uuid:uuid>/publish/", views.project_publish, name="project_publish"),
    path("<uuid:uuid>/unpublish/", views.project_unpublish, name="project_unpublish"),
]
