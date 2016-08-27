# Date of creation: 17.08.2016
# Date of last modification: 17.08.2016
# Author:
# Author last edited:
# Name: views.py
# Description: ---

# import lib
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here
# Вспомогательные функции
def get_list(model, *field):
    """Загрузить список записей из БД"""
    records_from_db = model.objects.values(*field)
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
    return render(HttpRequest, "firstApp/tasks.html", {"task_list": task_list})

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
    return render(HttpRequest, "firstApp/details_about_the_task.html", {"task": task, "users_task": users_task})

def upload_task(HttpRequest, task_id):
    """Загрузить данные в форму для указанной задачи"""
    task = Quest.objects.get(pk=task_id)
    users_list = get_list(Person, "id", "first_name", "last_name")
    users_task = []
    users_not_task = []
    for user in RunQuest.objects.filter(quest_id=task.id):
        users_task.append\
            ({
                "id": user.person.id,
                "first_name": user.person.first_name,
                "last_name": user.person.last_name
            })
    users_not_task = [x for x in users_list if x not in users_task]
    return render(HttpRequest, "firstApp/upload_task.html",
                  {
                      "task": task,
                      "users_not_task": users_not_task,
                      "users_task": users_task
                  })

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
    user_list = get_list(Person, "id", "first_name", "last_name")
    return render(HttpRequest, "firstApp/users.html", {"user_list": user_list})

def details_about_the_user(HttpRequest, user_id):
    """Отобразить подробную информацию о пользователе"""
    try:
        user = Person.objects.get(pk=user_id)
    except Quest.DoesNotExist:
        return HttpResponseNotFound("Пользователь с указанным id = " + user_id + " не найден!")
    return render(HttpRequest, "firstApp/details_about_the_user.html", {"user": user})

def delete_user(HttpRequest, task_id, user_id):
    """Удалить пользователя из задачи"""
    try:
        task = Quest.objects.get(pk=task_id)
    except Quest.DoesNotExist:
        return HttpResponseNotFound("Задача с указанным id = " + task_id + " не найдена!")
    user = RunQuest.objects.get(quest_id=task_id, person_id=user_id)
    user.delete()
    return render(HttpRequest, "firstApp/upload_task.html")


def meetings(HttpRequest):
    m = get_list(Meeting, "id", "date")
    args = {}
    args['meetings'] = m
    return render(HttpRequest, "firstApp/meetings.html", args)

def meeting_add(HttpRequest):
    if HttpRequest.method == "POST":
        form = MeetingForm(HttpRequest.POST)
        if form.is_valid():
            m = Meeting(title=form.cleaned_data['title'], target=form.cleaned_data['target'], text=form.cleaned_data['text'], date=form.cleaned_data['date'], place=form.cleaned_data['place'])
            m.save()

            for q in HttpRequest.POST.getlist('quest'):
                p = Plan(meeting=m, quest_id=q)
                p.save()
                quest = Quest.objects.get(pk=q)
                for p in quest.person.all():
                    j = Journal(meeting=m, person_id=p.id)
                    j.save()

            '''
            for p in HttpRequest.POST.getlist('person'):
                j = Journal(meeting=m, person_id=p)
                j.save()
            '''
            return redirect("/firstApp/meeting/{0}/".format(m.id))
    else:
        form = MeetingForm()
        return render(HttpRequest, "firstApp/meeting_add.html", { 'form': form })

def meeting_edit(HttpRequest, meeting_id):
    if HttpRequest.method == "POST":
        form = MeetingForm(HttpRequest.POST)
        if form.is_valid():

            m = Meeting.objects.get(pk=meeting_id)
            m.title=form.cleaned_data['title']
            m.target=form.cleaned_data['target']
            m.text=form.cleaned_data['text']
            m.date=form.cleaned_data['date']
            m.place=form.cleaned_data['place']
            m.save() 

            Plan.objects.filter(meeting_id=meeting_id).delete()
            Journal.objects.filter(meeting_id=meeting_id).delete()

            for q in HttpRequest.POST.getlist('quest'):
                p = Plan(meeting=m, quest_id=q)
                p.save()
                quest = Quest.objects.get(pk=q)
                for p in quest.person.all():
                    j = Journal(meeting=m, person_id=p.id)
                    j.save()
            
            return redirect("/firstApp/meeting/{0}/".format(m.id))
    else:
        m = Meeting.objects.get(pk=meeting_id)
        form = MeetingForm(initial={'title': m.title, 'target': m.target, 'text': m.text, 'date': m.date, 'place': m.place}, instance=m)
        return render(HttpRequest, "firstApp/meeting_edit.html", { 'form': form })

def meeting_info(HttpRequest, meeting_id):
    m = Meeting.objects.get(id=meeting_id)
    args = {}
    args['meeting'] = m
    args['quest'] = m.quest.values()
    args['person'] = m.person.values()
    return render(HttpRequest, "firstApp/meeting_info.html", args)   

def meeting_delete(HttpRequest, meeting_id):
    Plan.objects.filter(meeting_id=meeting_id).delete()
    Journal.objects.filter(meeting_id=meeting_id).delete()
    Meeting.objects.get(id=meeting_id).delete()

    return redirect("/firstApp/meetings/") 