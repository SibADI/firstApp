# Date of creation: 17.08.2016
# Date of last modification: 17.08.2016
# Author:
# Author last edited:
# Name: views.py
# Description: ---

# import lib
from django.shortcuts import render

# Create your views here
def index(request):
    """Стартовая страница приложения"""
    return render(request, "firstApp/index.html")