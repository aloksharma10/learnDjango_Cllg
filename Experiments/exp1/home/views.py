from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home.models import User
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

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')
        print(name, email, phone, content)
        user=User(name=name, email=email, phone=phone, content=content)
        user.save()
    return render(request, 'contact.html')
    
def getUser(request):
    users = User.objects.all()
    return render(request, 'user.html', {'users': users})

def getParam(request, slug):
    return HttpResponse(f"Your slug is {slug}.")