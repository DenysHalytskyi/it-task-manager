from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from django.views import generic

from manager.models import Task, Worker, Position, TaskType


def index(request: HttpRequest) -> HttpResponse:
    num_tasks = Task.objects.all().count()
    num_workers = Worker.objects.all().count()
    context = {
        "num_tasks": num_tasks,
        "num_workers": num_workers,
    }
    return render(request, "manager/index.html", context=context)

"""List views"""
class WorkerListView(generic.ListView):
    model = Worker
    context_object_name = "worker_list"


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"


class PositionListView(generic.ListView):
    model = Position
    context_object_name = "position_list"


class TaskTypeListView(generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "manager/task_type_list.html"

"""Detail views"""
def worker_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        worker = Worker.objects.get(id=pk)
    except Worker.DoesNotExist:
        raise Http404("Worker does not exist")
    context = {
        "worker": worker,
    }

    return render(request, "manager/worker_detail.html", context=context)
