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
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	vk = models.URLField(max_length=50)
	login = models.CharField(max_length=50)
	password = models.CharField(max_length=32)

	def __str__(self):
		return ' '.join([self.first_name, self.last_name,])

# Системный журнал
class SysJournal(models.Model):
	datein = models.DateTimeField()
	dateout = models.DateTimeField()
	person = models.ForeignKey(Person, null='true')

# Задача
class Quest(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField()
	date = models.DateField(auto_now=True)
	status = models.IntegerField(default=3)
	person = models.ManyToManyField(Person, through='RunQuest')

	def __str__(self):
		return self.title

# Активная задача
class RunQuest(models.Model):
	person = models.ForeignKey(Person, null='true')
	quest = models.ForeignKey(Quest, null='true')
	comment = models.TextField()
	first_date = models.DateField()
	last_date = models.DateField()

# Встреча
class Meeting(models.Model):
	title = models.CharField(max_length=255)
	target = models.CharField(max_length=255)
	text = models.TextField()
	date = models.DateTimeField()
	place = models.CharField(max_length=255)
	quest = models.ManyToManyField(Quest, through='Plan')
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