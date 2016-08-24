# Date of creation: 17.08.2016
# Date of last modification: 17.08.2016
# Author:
# Author last edited:
# Name: views.py
# Description: ---

# import lib
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Quest, RunQuest, Person

# Create your views here
# Вспомогательные функции
def get_list(model):
    """Загрузить список записей из БД"""
    records_from_db = model.objects.values()
    records = []
    for current_record in records_from_db:
        records.append(current_record)
    return records

def index(HttpRequest):
    """Отобразить стартовую страницу"""
    return render(HttpRequest, "firstApp/index.html")

def tasks(HttpRequest):
    """Отобразить список задач"""
    task_list = get_list(Quest)
    return render(HttpRequest, "firstApp/tasks.html", {'task_list': task_list})

def details_about_the_task(HttpRequest, task_id):
    """Отобразить подробную информацию о задачи"""
    try:
        task = Quest.objects.get(pk=task_id)
    except Quest.DoesNotExist:
        return HttpResponseNotFound("Задача с указанным id = " + task_id + " не найдена!")
    users_task = []
    for user in RunQuest.objects.filter(quest_id=task.id):
        users_task.append\
            ({
                "id": user.person.id,
                "first_name": user.person.first_name,
                "last_name": user.person.last_name
            })
    return render(HttpRequest, "firstApp/details_about_the_task.html", {'task': task, "users_task": users_task})

def upload_task(HttpRequest, task_id):
    """Загрузить данные в форму для указанной задачи"""
    task = Quest.objects.get(pk=task_id)
    users_list = get_list(Person)
    users_task = []
    users_temp = []
    users = []
    for user in RunQuest.objects.filter(quest_id=task.id):
        users_task.append\
            ({
                "id": user.person.id,
                "first_name": user.person.first_name,
                "last_name": user.person.last_name
            })
    for user in users_list:
        for user_task in users_task:
            if (user["id"] == user_task["id"]):
                users_temp.append(user)
                continue
            continue
    users = [x for x in users_list if x not in users_temp]
    return render(HttpRequest, "firstApp/upload_task.html", {'task': task, "users": users, "users_task": users_task})

def edit_task_id(HttpRequest, task_id):
    """Обновить данные в БД для указанной задачи"""
    Quest.objects.filter(pk=task_id).update\
        (
            id=HttpRequest.POST["id"],
            title=HttpRequest.POST["title"],
            text=HttpRequest.POST["text"],
            status=HttpRequest.POST["status"]
        )
    return HttpResponseRedirect("/firstApp/tasks")

def delete_the_task(HttpRequest, task_id):
    """Удалить указанную задачу"""
    task = Quest.objects.get(pk=task_id)
    task.delete()
    return HttpResponseRedirect("/firstApp/tasks")

def users(HttpRequest):
    """Отобразить список пользователей"""
    user_list = get_list(Person)
    return render(HttpRequest, "firstApp/users.html", {'user_list': user_list})

def details_about_the_user(HttpRequest, user_id):
    """Отобразить подробную информацию о пользователе"""
    try:
        user = Person.objects.get(pk=user_id)
    except Quest.DoesNotExist:
        return HttpResponseNotFound("Пользователь с указанным id = " + user_id + " не найден!")
    return render(HttpRequest, "firstApp/details_about_the_user.html", {'user': user})

def delete_user(HttpRequest, task_id, user_id):
    """Удалить пользователя из задачи"""
    try:
        task = Quest.objects.get(pk=task_id)
    except Quest.DoesNotExist:
        return HttpResponseNotFound("Задача с указанным id = " + task_id + " не найдена!")
    user = RunQuest.objects.get(quest_id=task_id, person_id=user_id)
    user.delete()
    return render(HttpRequest, "firstApp/upload_task.html")