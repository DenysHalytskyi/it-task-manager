from django.urls import path

from manager.views import (
    index,
    WorkerListView,
    TaskListView,
    PositionListView,
    TaskTypeListView,
    worker_detail_view,
    task_detail_view,
    position_detail_view,
    task_type_detail_view,
    TaskCreateView,
    )

app_name = "manager"
urlpatterns = [
    path("", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("positions/", PositionListView.as_view(), name="position-list"),
    path("task_types/", TaskTypeListView.as_view(), name="task-type-list"),

    path("workers/<int:pk>/", worker_detail_view, name="worker-detail"),
    path("tasks/<int:pk>/", task_detail_view, name="task-detail"),
    path("positions/<int:pk>/", position_detail_view, name="position-detail"),
    path("task_types/<int:pk>/", task_type_detail_view, name="task-type-detail"),

    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
]
