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
    TaskUpdateView,
    TaskDeleteView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
    TaskTypeDeleteView,
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
    path("task_types/create/", TaskTypeCreateView.as_view(), name="task-type-create"),

    path ("tasks/update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("task_types/update/<int:pk>/", TaskTypeUpdateView.as_view(), name="task-type-update"),

    path("tasks/delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("task_types/delete/<int:pk>/", TaskTypeDeleteView.as_view(), name="task-type-delete"),
]
