from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from manager.models import Task, Worker


def index(request: HttpRequest) -> HttpResponse:
    num_tasks = Task.objects.all().count()
    num_workers = Worker.objects.all().count()
    context = {
        "num_tasks": num_tasks,
        "num_workers": num_workers,
    }
    return render(request, "manager/index.html", context=context)


class WorkerListView(generic.ListView):
    model = Worker
    context_object_name = "worker_list"


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
