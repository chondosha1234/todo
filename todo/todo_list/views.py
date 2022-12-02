from django.shortcuts import render
from todo_list.models import Task, Completed
from todo_list.forms import *
from django.http import HttpResponseRedirect

# Create your views here.
def todo_list(request):
    tasks = Task.objects.all()
    forms = []
    for t in tasks:
        form = TaskForm(complete=t.complete, description=t.description, id=t.id)
        forms.append(form)
    context = {
        'forms': forms,
    }
    return render(request, 'list.html', context)


def add_task(request):
    if 'add-description' in request.POST:
        task = Task(description=request.POST['add-description'])
        task.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def delete_task(request):
    if 'delete-id' in request.POST:
        task = Task.objects.get(id=request.POST['delete-id'])
        if task:
          task.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def edit_task(request):
    if 'edit-id' and 'edit-description' in request.POST:
        task = Task.objects.get(id=request.POST['edit-id'])
        if task:
          task.description = request.POST['edit-description']
          task.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def completed_tasks(request):
    tasks = Completed.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'completed.html', context)


def complete(request, id):
    task = Task.objects.get(pk=id)

    if 'complete' in request.POST:
        task.complete = True
        completed_task = Completed(description=task.description, task_id=id)
        completed_task.save()
    else:
        task.complete = False
        completed_task = Completed.objects.get(task_id=id)
        completed_task.delete()

    task.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
