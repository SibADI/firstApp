# Date of creation: 17.08.2016
# Date of last modification: 17.08.2016
# Author: Alexander ATOMIC Miller
# Author last edited: Alexander ATOMIC Miller
# Name: urls.py
# Description: ---

# import lib
from django.conf.urls import include, url
from django.contrib import admin

# Setting URL for this project
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^firstApp/', include('firstApp.urls')),
]