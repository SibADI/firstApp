# Date of creation: 17.08.2016
# Date of last modification: 17.08.2016
# Author:
# Author last edited:
# Name: urls.py
# Description: ---

# import lib
from django.conf.urls import url
from . import views

# Create your models here
# Setting URL for this application
app_name = 'firstApp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]