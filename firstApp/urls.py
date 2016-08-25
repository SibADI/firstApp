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
urlpatterns = \
    [
        url(r'^$', views.index, name='index'),
        url(r'^users/$', views.users, name='users'),
        url(r'^users/(?P<LoginUser>[^/]+)/$', views.about_user, name='about_user'),
        url(r'^users/(?P<LoginUser>[^/]+)/edit/$', views.edit_user, name='edit_user'),
        url(r'^tasks/$', views.tasks, name='tasks'),
        url(r'^tasks/(?P<TaskID>[0-9]+)/$', views.about_task, name='about_task'),
        url(r'^tasks/(?P<TaskID>[0-9]+)/edit$', views.edit_task, name='edit_task'),
    ]