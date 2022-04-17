import import_export.formats.base_formats
from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from .models import Month, Task
from .forms import TaskForm


# Create your views here.
def index(request):
    return render(request, 'tasks/index.html')


def task_list(request, month=None):
    if month is None:
        return redirect('task-list', month=timezone.now().month)
    months = Month.objects.all()
    selected_month = months.get(number=month)
    tasks = Task.objects.filter(month=selected_month)
    # pending_tasks = [task for task in tasks if task.status == 'pending']
    # in_progress_tasks = [task for task in tasks if task.status == 'in-progress']
    # complete_tasks = [task for task in tasks if task.status == 'complete']
    context = {
        'months': months,
        'selected_month': selected_month,
        'tasks': tasks,
    }
    if request.META.get('HTTP_HX_REQUEST'):
        return render(request, 'tasks/partials/task_list_partial.html', context)
    else:
        return render(request, 'tasks/task_list.html', context)


def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    context = {
        'task': task,
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse(headers={'HX-Trigger': 'taskListChanged'})

    if request.method == 'DELETE':
        task.delete()
        return HttpResponse(headers={'HX-Trigger': 'taskListChanged'})

    return render(request, 'tasks/partials/forms/task_update_modal.html', context)


def task_create(request):
    form = TaskForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse(headers={'HX-Trigger': 'taskListChanged'})
        return render(request, 'tasks/partials/forms/task_create_modal.html', context)

    if request.method == 'GET' and request.META.get('HTTP_HX_REQUEST'):
        return render(request, 'tasks/partials/forms/task_create_modal.html', context)
    else:
        return redirect('index')  # prevent users from reaching standalone form
