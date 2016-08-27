# Date of creation: 25.08.2016
# Date of last modification: 25.08.2016
# Author:
# Author last edited:
# Name: views.py
# Description: ---

# import lib
from .models import *
from django import forms
from django.forms import ModelForm

class PersonForm(forms.Form):
    login = forms.CharField\
        (
            label="Логин:",
            max_length=50,
            required=True
        )
    first_name = forms.CharField\
        (
            label="Имя:",
            max_length=50,
            required=True
        )
    last_name = forms.CharField\
        (
            label="Фамилия:",
            max_length=50,
            required=True
        )
    email = forms.EmailField\
        (
            label="Email:",
            max_length=50,
            required=True
        )
    vk = forms.URLField\
        (
            label="ВКонтакте:",
            max_length=50,
            required=False
        )
    password = forms.CharField\
        (
            widget=forms.PasswordInput(attrs={"class":"class"}), # CSS - Гордиенко
            label="Пароль:",
            max_length=32,
            required=True
        )

class QuestForm(forms.Form):
    STATUS = \
        (
            (1, 'Закрыта'),
            (2, 'Заблокирована'),
            (3, 'Активна')
        )
    title = forms.CharField\
        (
            label="Название задачи:",
            max_length=50,
            required=True
        )
    text = forms.CharField\
        (
            widget=forms.Textarea,
            label="Описание задачи:",
            max_length=255,
            required=False
        )
    date = forms.DateField\
        (
            label="Дата создания задачи:",
            input_formats=['%Y-%m-%d'],
            required=True
        )
    status = forms.ChoiceField\
        (
            widget=forms.RadioSelect,
            choices=STATUS,
            required=True
        )
    person = forms.ModelMultipleChoiceField\
        (
            queryset=Person.objects.all(),
            required=False
        )


class MeetingForm(ModelForm):
	class Meta:
		model = Meeting
		fields = ('title', 'target', 'text', 'date', 'place', 'quest')
		#fields = "__all__"