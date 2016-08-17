# Date of creation: 17.08.2016
# Date of last modification: 17.08.2016
# Author: Alexander ATOMIC Miller
# Author last edited: Alexander ATOMIC Miller
# Name: models.py
# Description: ---

# import lib
from django.db import models

# Create your models here
# Question
class Question(models.Model):
    question_text = models.CharField("Question", max_length=255)
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        """Returns the value of the field 'question_text'"""
        return self.question_text

# Choice
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField("Choice", max_length=255)
    votes = models.IntegerField("Votes", default=0)

    def __str__(self):
        """Returns the value of the field 'choice_text'"""
        return self.choice_text