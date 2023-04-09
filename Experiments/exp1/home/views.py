from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def index(request):
    name = {'Name': 'Alok Sharma'}
    enroll = {'Enroll': '02211102021'}

    now = datetime.now()
    if now.hour < 12:
        greeting = 'Good morning'
    elif now.hour < 18:
        greeting = 'Good afternoon'
    else:
        greeting = 'Good evening'
    return render(request, 'index.html', {'greeting': greeting, 'Name': name, 'Enroll': enroll})


def dynamicData(request):
    now = datetime.now()
    return render(request, 'date.html', {'date': now})

