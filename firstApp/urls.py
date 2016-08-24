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
    url(r'^$', views.home, name='home'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^tasks/(?P<task_id>[0-9]+)/$', views.details_about_the_task, name='details_about_the_task'),
    url(r'^tasks/(?P<task_id>[0-9]+)/edit/$', views.ulpoad_task, name='ulpoad_task'),
    url(r'^tasks/(?P<task_id>[0-9]+)/edit_id/$', views.edit_task_id, name='edit_task_id'),
    url(r'^tasks/(?P<task_id>[0-9]+)/delete$', views.delete_the_task, name='delete_the_task'),
    url(r'^users/$', views.users, name='users'),
    url(r'^users/(?P<user_id>[0-9]+)/$', views.details_about_the_user, name='details_about_the_user'),
]