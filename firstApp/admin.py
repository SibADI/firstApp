# Date of creation: 17.08.2016
# Date of last modification: 17.08.2016
# Author: Alexander ATOMIC Miller
# Author last edited: Alexander ATOMIC Miller
# Name: admin.py
# Description: ---

# import lib
from django.contrib import admin
from .models import Question, Choice

# Register your models here
# Adding items in the admin panel
admin.site.register(Question)
admin.site.register(Choice)
