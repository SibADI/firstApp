# Date of creation: 17.08.2016
# Date of last modification: 17.08.2016
# Author:
# Author last edited:
# Name: views.py
# Description: ---

# import lib
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from .models import Quest

# Create your views here
# Вспомогательные функции
def list(model):
    """Отображение спика записей для указанной модели"""
    records_from_db = model.objects.values()
    records = []
    for current_record in records_from_db:
        records.append(current_record)
    return records

# Основная логика
def index(request):
    """Стартовая страница приложения"""
    return render(request, "firstApp/index.html")

def tasks(request):
    """Отображение списка задач"""
    list_tasks = list(Quest)
    return render(request, "firstApp/tasks.html", {'tasks': list_tasks})

def detail_task(request, task_id):
    """Отображение подробной информации о выбранной задачи"""
    try:
        task = Quest.objects.get(pk = task_id)
    except Quest.DoesNotExist:
        return HttpResponseNotFound("Не найдено!")
    return render(request, "firstApp/detail.html", {'task': task})

def edit_task(request, task_id):
    """Отображение подробной информации о выбранной задачи"""
    task = Quest.objects.get(pk=task_id)
    return render(request, "firstApp/edit.html", {'task': task})

def edit_task_id(request, task_id):
    """Отображение подробной информации о выбранной задачи"""
    Quest.objects.filter(pk=task_id).update\
        (
            id = request.POST["id"],
            title = request.POST["title"],
            text = request.POST["text"],
            status = request.POST["status"]
        )
    return HttpResponseRedirect("/firstApp/tasks");

def delete_task(request, task_id):
    """Отображение подробной информации о выбранной задачи"""
    task = Quest.objects.get(pk=task_id)
    task.delete()
    return HttpResponseRedirect("/firstApp/tasks");