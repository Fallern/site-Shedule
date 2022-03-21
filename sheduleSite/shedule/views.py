from django.shortcuts import render
import datetime

# Create your views here.


def index(request):
    """Home page apps shedule"""

    return render(request, 'shedule/index.html')