from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from manager.forms import TaskForm, WorkerCreateForm, WorkerUpdateForm
from manager.models import Task, Worker, Position, TaskType


def index(request: HttpRequest) -> HttpResponse:
    num_tasks = Task.objects.all().count()
    num_workers = Worker.objects.all().count()
    context = {
        "num_tasks": num_tasks,
        "num_workers": num_workers,
    }
    return render(request, "manager/index.html", context=context)


class SignUpView(generic.CreateView):
    form_class = WorkerCreateForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

"""List views"""
class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = "worker_list"


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "task_list"


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    context_object_name = "position_list"


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    context_object_name = "task_type_list"
    template_name = "manager/task_type_list.html"


"""Detail views"""
@login_required
def worker_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        worker = Worker.objects.get(id=pk)
    except Worker.DoesNotExist:
        raise Http404("Worker does not exist")
    context = {
        "worker": worker,
    }

    return render(request, "manager/worker_detail.html", context=context)


@login_required
def task_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        raise Http404("Task does not exist")
    context = {
        "task": task,
    }

    return render(request, "manager/task_detail.html", context=context)


@login_required
def position_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        position = Position.objects.get(id=pk)
    except Position.DoesNotExist:
        raise Http404("Position does not exist")
    context = {
        "position": position,
    }

    return render(request, "manager/position_detail.html", context=context)


@login_required
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
class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task-list")
    template_name = "manager/task_form.html"


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("manager:task-type-list")
    template_name = "manager/task_type_form.html"


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("manager:position-list")
    template_name = "manager/position_form.html"


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreateForm
    success_url = reverse_lazy("manager:index")
    template_name = "manager/worker_form.html"


"""Update views"""
class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:task-list")
    template_name = "manager/task_form.html"


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    success_url = reverse_lazy("manager:task-type-list")
    template_name = "manager/task_type_form.html"


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("manager:position-list")
    template_name = "manager/position_form.html"


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("manager:worker-list")
    template_name = "manager/worker_form.html"


"""Delete views"""
class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:task-list")
    template_name = "manager/task_confirm_delete.html"


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    success_url = reverse_lazy("manager:task-type-list")
    template_name = "manager/task_type_confirm_delete.html"


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("manager:position-list")
    template_name = "manager/position_confirm_delete.html"


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("manager:index")
    template_name = "manager/worker_confirm_delete.html"
