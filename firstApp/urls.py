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
        url(r'^users/(?P<LoginUser>[^/]+)/tasks$', views.tasks_user, name='tasks_user'),
        url(r'^tasks/$', views.tasks, name='tasks'),
        url(r'^tasks/(?P<TaskID>[0-9]+)/$', views.about_task, name='about_task'),
        url(r'^tasks/add$', views.add_task, name='add_task'),
        url(r'^tasks/(?P<TaskID>[0-9]+)/edit$', views.edit_task, name='edit_task'),
        url(r'^tasks/(?P<TaskID>[0-9]+)/delete$', views.delete_task, name='delete_task'),
        url(r'^meetings/$', views.meetings, name='meetings'),
        url(r'^meeting/(?P<meeting_id>[0-9]+)/$', views.meeting_info, name='meeting_info'),
        url(r'^meeting_add/$', views.meeting_add, name='meeting_add'),
        url(r'^meeting_edit/(?P<meeting_id>[0-9]+)/$', views.meeting_edit, name='meeting_edit'),
        url(r'^meeting_delete/(?P<meeting_id>[0-9]+)/$', views.meeting_delete, name='meeting_delete'),
    ]