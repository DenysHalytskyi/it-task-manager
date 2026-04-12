from django.urls import path

from manager.views import index, WorkerListView

app_name = "manager"
urlpatterns = [
    path("home/", index, name="index"),
    path("workers/", WorkerListView.as_view(), name="worker-list"),
]