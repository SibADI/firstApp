# Date of creation: 17.08.2016
# Date of last modification: 17.08.2016
# Author:
# Author last edited:
# Name: views.py
# Description: ---

# import lib
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404
from .models import Person

# Create your views here
# Стартовая страница
def index(request):
    return render(request, "firstApp/index.html")

# Стартовая страница
def add_person(request):
    if (request.method == "POST"):
        person = Person(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            login = request.POST['login'],
            email = request.POST['email'],
            vk = request.POST['vk'],
            password = request.POST['password']
        )
        person.save()
        return HttpResponseRedirect("/firstApp/")
    else:
        return render(request, "firstApp/add.html")

# Список пользователей для редактирования
def edit_person(request):
    value = Person.objects.values()
    array_person = []
    for person in value:
        array_person.append(person)
    return render(request, "firstApp/edit.html", {'arrayPerson': array_person})

# Редактирование пользователя
def edit_person_id(request, person_id):
    if (request.method == "GET"):
        try:
            person = Person.objects.get(pk=person_id)
        except Person.DoesNotExist:
            raise Http404("Person does not exist")
        return render(request, "firstApp/edit_user.html", {'person': person})
    else:
        person = Person.objects.get(pk=person_id)
        person.first_name = request.POST['first_name'],
        person.last_name = request.POST['last_name'],
        person.login = request.POST['login'],
        person.email = request.POST['email'],
        person.vk = request.POST['vk'],
        person.password = request.POST['password']
        person.save()
        return HttpResponseRedirect("/firstApp/")

# Список пользователей для удаления
def delete_person(request):
    value = Person.objects.values()
    array_person = []
    for person in value:
        array_person.append(person)
    return render(request, "firstApp/delete.html", {'arrayPerson': array_person})

# Удаление конкретного пользователя
def delete_person_id(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
        person.delete()
        return HttpResponseRedirect("/firstApp/")
    except Person.DoesNotExist:
        raise Http404("Person does not exist")