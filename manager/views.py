from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from manager.models import Task, Worker


def index(request: HttpRequest) -> HttpResponse:
    num_tasks = Task.objects.all().count()
    num_workers = Worker.objects.all().count()
    context = {
        "num_tasks": num_tasks,
        "num_workers": num_workers,
    }
    return render(request, "manager/index.html", context=context)
