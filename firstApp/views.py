# Date of creation: 17.08.2016
# Date of last modification: 17.08.2016
# Author:
# Author last edited:
# Name: views.py
# Description: ---

# import lib
from .forms import *
from .models import *
from django.http import *
from django.shortcuts import *

def get_list(model, *field):
    """Загрузить список записей из БД"""
    records_from_db = model.objects.values(*field)
    records = []
    for current_record in records_from_db:
        records.append(current_record)
    return records

# Create your views here
def index(HttpRequest):
    """Отобразить стартовую страницу"""
    return render(HttpRequest, "firstApp/index.html")

# Баги:
# - Рефакторинг кода
def users(HttpRequest):
    """Отобразить список всех пользователей"""
    try:
        users = Person.objects.values("login", "first_name", "last_name")
    except:
        return HttpResponseServerError("Server error!")
    return render(HttpRequest, "firstApp/users.html",
                  {
                      "users": users
                  })

# Баги:
# - Нет фото пользователя
# - Рефакторинг кода
def about_user(HttpRequest, LoginUser):
    """Отобразить подробную информацию о пользователе"""
    try:
        user = Person.objects.values\
        (
            "login", "first_name", "last_name", "email", "vk"
        ).get(login=LoginUser)
    except:
        return HttpResponseNotFound("Not found!")
    return render(HttpRequest, "firstApp/about_user.html",
                  {
                      "user": user
                  })

# Баги:
# - Рефакторинг кода
def edit_user(HttpRequest, LoginUser):
    """Редактировать пользователя"""
    if (HttpRequest.method == "POST"):
        user = PersonForm(HttpRequest.POST)
        if user.is_valid():
            try:
                user_db = Person.objects.filter(login=LoginUser)
            except:
                return HttpResponseServerError("Server error!")
            user_db.update\
                (
                    login=user.cleaned_data["login"],
                    first_name=user.cleaned_data["first_name"],
                    last_name=user.cleaned_data["last_name"],
                    email=user.cleaned_data["email"],
                    vk=user.cleaned_data["vk"],
                    password=user.cleaned_data["password"]
                )
            return HttpResponseRedirect("/firstApp/")
        else:
            return HttpResponseBadRequest("Bad request!")
    else:
        try:
            user = PersonForm(initial=Person.objects.values().get(login=LoginUser))
        except:
            return HttpResponseServerError("Server error!")
        return render(HttpRequest, "firstApp/edit_user.html",
                      {
                          "user": user,
                          "login": LoginUser
                      })

# Баги:
# - Рефакторинг кода
def tasks(HttpRequest):
    """Отобразить список всех задач"""
    try:
        tasks = Quest.objects.values("id", "title", "date", "status")
    except:
        return HttpResponseServerError("Server error!")
    return render(HttpRequest, "firstApp/tasks.html",
                  {
                      "tasks": tasks
                  })

# Баги:
# - Рефакторинг кода
def tasks_user(HttpRequest, LoginUser):
    """Отобразить список всех задач для конкретного пользователя"""
    try:
        user = Person.objects.get(login=LoginUser)
    except:
        HttpResponseNotFound("Not found!")
    try:
        run_quest_tasks = RunQuest.objects.filter(person_id=user.id).values()
    except:
        return HttpResponseServerError("Server error!")
    tasks_user = []
    try:
        for task in run_quest_tasks:
            tasks_user.append(Quest.objects.values("id", "title", "date", "status").get(id=task["quest_id"]))
    except:
        HttpResponseNotFound("Not found!")
    return render(HttpRequest, "firstApp/tasks_user.html",
                  {
                      "tasks_user": tasks_user
                  })

# Баги:
# - Рефакторинг кода
def about_task(HttpRequest, TaskID):
    """Отобразить подробную информацию о задаче"""
    try:
        task = Quest.objects.values().get(id=TaskID)
        current_users = RunQuest.objects.filter(quest_id=TaskID).values()
    except:
        return HttpResponseNotFound("Not found!")
    users = []
    try:
        for user in current_users:
            users.append(Person.objects.values("login", "first_name", "last_name").get(id=user["person_id"]))
    except:
        return HttpResponseNotFound("Not found!")
    return render(HttpRequest, "firstApp/about_task.html",
                  {
                      "task": task,
                      "users": users
                  })

# Баги:
# - Сделать безопасное сохранение new_run_quest_user.save()
# - Реализовать наследование first_date от Quest
# - Реализовать другой способ включения пользователей в проект new_run_quest_user = RunQuest
# - Реализовать подсказку для Date(форматы, всп. меню)
# - Рефакторинг кода
def add_task(HttpRequest):
    """Редактировать задачу"""
    if (HttpRequest.method == "POST"):
        task = QuestForm(HttpRequest.POST)
        if task.is_valid():
            new_task_db = Quest\
                (
                    title=task.cleaned_data["title"],
                    text=task.cleaned_data["text"],
                    date=task.cleaned_data["date"],
                    status=task.cleaned_data["status"],
                )
            try:
                new_task_db.save()
            except:
                return HttpResponseNotModified("Not modified!")
            try:
                for user in task.cleaned_data["person"]:
                    new_run_quest_user = RunQuest\
                        (
                            first_date=task.cleaned_data["date"],
                            last_date=task.cleaned_data["date"],
                            quest_id=new_task_db.id,
                            person_id=user.id
                        )
                    new_run_quest_user.save()
            except:
                return HttpResponseNotModified("Not modified!")
            return HttpResponseRedirect("/firstApp/")
        else:
            return HttpResponseBadRequest("Bad request!")
    else:
        try:
            task = QuestForm()
        except:
            return HttpResponseServerError("Server error!")
        return render(HttpRequest, "firstApp/add_task.html",
                      {
                          "task": task
                      })

# Баги:
# - Сделать безопасное удаление RunQuest.objects.filter(quest_id=TaskID).delete()
# - Сделать безопасное сохранение new_run_quest.save()
# - Реализовать наследование first_date от Quest
# - Реализовать другой способ включения пользователей в проект new_run_quest = RunQuest
# - Реализовать подсказку для Date(форматы, всп. меню)
# - Рефакторинг кода
def edit_task(HttpRequest, TaskID):
    """Редактировать задачу"""
    if (HttpRequest.method == "POST"):
        task = QuestForm(HttpRequest.POST)
        if task.is_valid():
            task_db = Quest.objects.filter(pk=TaskID)
            task_db.update\
                (
                    title=task.cleaned_data["title"],
                    text=task.cleaned_data["text"],
                    date=task.cleaned_data["date"],
                    status=task.cleaned_data["status"],
                )
            try:
                RunQuest.objects.filter(quest_id=TaskID).delete()
            except:
                return HttpResponseNotModified("Not modified!")
            try:
                for user in task.cleaned_data["person"]:
                    new_run_quest_user = RunQuest\
                        (
                            first_date=task.cleaned_data["date"],
                            last_date=task.cleaned_data["date"],
                            quest_id=TaskID,
                            person_id=user.id
                        )
                    new_run_quest_user.save()
            except:
                return HttpResponseNotModified("Not modified!")
            return HttpResponseRedirect("/firstApp/")
        else:
            return HttpResponseBadRequest("Bad request!")
    else:
        try:
            task = QuestForm(initial=Quest.objects.values().get(pk=TaskID))
        except:
            return HttpResponseNotFound("Not found!")
        return render(HttpRequest, "firstApp/edit_task.html",
                      {
                          "task": task,
                          "task_id": TaskID
                      })

# Баги:
# - Рефакторинг кода
def delete_task(HttpRequest, TaskID):
    """Удалить задачу"""
    try:
        task = Quest.objects.get(pk=TaskID)
    except:
        return HttpResponseNotFound("Not found!")
    try:
        task.delete()
    except:
        return HttpResponseNotModified("Not modified!")
    return HttpResponseRedirect("/firstApp/")

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