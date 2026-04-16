from django.urls import path

from apps.projects import views

app_name = "projects"

urlpatterns = [
    path("", views.ProjectListView.as_view(), name="project_list"),
    path("new/", views.project_create, name="project_create"),
    path("<uuid:uuid>/editor/", views.ProjectEditorView.as_view(), name="project_editor"),
    path("<uuid:uuid>/publish/", views.project_publish, name="project_publish"),
    path("<uuid:uuid>/unpublish/", views.project_unpublish, name="project_unpublish"),
]
