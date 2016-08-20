# Date of creation: 17.08.2016
# Date of last modification: 17.08.2016
# Author:
# Author last edited:
# Name: views.py
# Description: ---

# import lib
from django.http import HttpResponse

# Create your views here
# Home applications
def index(request):
    """Home applications"""
    return HttpResponse("Hello, world!")