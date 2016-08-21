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
    url(r'^addPerson/$', views.add_person, name='add_person'),
    url(r'^editPerson/$', views.edit_person, name='edit_person'),
    url(r'^editPerson/(?P<person_id>[0-9]+)/$', views.edit_person_id, name='edit_person_id'),
    url(r'^deletePerson/$', views.delete_person, name='delete_person'),
    url(r'^deletePerson/(?P<person_id>[0-9]+)/$', views.delete_person_id, name='delete_person_id'),
]