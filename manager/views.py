from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TaskForm
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


def task_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    context = {
        "task": task,
    }

    return render(request, "manager/task_detail.html", context=context)


def position_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        position = Position.objects.get(id=pk)
    except Position.DoesNotExist:
        raise Http404("Position does not exist")
    context = {
        "position": position,
    }

    return render(request, "manager/position_detail.html", context=context)


def task_type_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        task_type = TaskType.objects.get(id=pk)
    except TaskType.DoesNotExist:
        raise Http404("Task does not exist")
    context = {
        "task_type": task_type,
    }

    return render(request, "manager/task_type_detail.html", context=context)

"""Create views"""
class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task-list")
    template_name = "manager/task_form.html"


class TaskTypeCreateView(generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("manager:task-type-list")
    template_name = "manager/task_type_form.html"

"""Update views"""
class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task-list")
    template_name = "manager/task_form.html"

"""Delete views"""
class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task-list")
    template_name = "manager/task_confirm_delete.html"