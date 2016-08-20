# Date of creation: 17.08.2016
# Date of last modification: 17.08.2016
# Author:
# Author last edited:
# Name: models.py
# Description: ---

# import lib
from django.db import models

# Create your models here

# Пользователь
class Person(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	vk = models.EmailField(max_length=50)
	login = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

	def __str__(self):
		return self.firstname + ' ' + self.lastname

# Системный журнал
class SysJournal(models.Model):
	datein = models.DateTimeField()
	dateout = models.DateTimeField()
	person = models.ForeignKey(Person, null='true')

# Задача
class Quest(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField()
	date = models.DateTimeField()
	status = models.IntegerField(default=0)

	models.ManyToManyField(Person, through='RunQuest')

	def __str__(self):
		return self.title

# Активная задача
class RunQuest(models.Model):
	person = models.ForeignKey(Person, null='true')
	quest = models.ForeignKey(Quest, null='true')
	comment = models.TextField()
	firstdate = models.DateTimeField()
	lastdate = models.DateTimeField()

# Встреча
class Meeting(models.Model):
	title = models.CharField(max_length=50)
	target = models.CharField(max_length=50)
	text = models.TextField()
	date = models.DateTimeField()
	place = models.CharField(max_length=50)

	plans = models.ManyToManyField(Quest, through='Plan')
	persons = models.ManyToManyField(Person, through='Journal')

	def __str__(self):
		return self.title

# Журнал
class Journal(models.Model):
	meeting = models.ForeignKey(Meeting, null='true')
	person = models.ForeignKey(Person, null='true')
	status = models.IntegerField(default=0)

# План
class Plan(models.Model):
	meeting = models.ForeignKey(Meeting, null='true')
	quest = models.ForeignKey(Quest, null='true')
	result = models.TextField()