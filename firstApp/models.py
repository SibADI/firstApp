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
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	vk = models.EmailField(max_length=255)
	login = models.CharField(max_length=255)
	password = models.CharField(max_length=255)

	def __str__(self):
		return ' '.join([self.first_name, self.last_name,])

# Системный журнал
class SysJournal(models.Model):
	datein = models.DateTimeField()
	dateout = models.DateTimeField()
	person = models.ForeignKey(Person, null='true')

# Задача
class Quest(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	date = models.DateTimeField()
	status = models.IntegerField(default=0)
	person = models.ManyToManyField(Person, through='RunQuest')

	def __str__(self):
		return self.title

# Активная задача
class RunQuest(models.Model):
	person = models.ForeignKey(Person, null='true')
	quest = models.ForeignKey(Quest, null='true')
	comment = models.TextField()
	first_date = models.DateTimeField()
	last_date = models.DateTimeField()

# Встреча
class Meeting(models.Model):
	title = models.CharField(max_length=255)
	target = models.CharField(max_length=255)
	text = models.TextField()
	date = models.DateTimeField()
	place = models.CharField(max_length=255)
	quest = models.ManyToManyField(Quest, through='Plan')
	person = models.ManyToManyField(Person, through='Journal')

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