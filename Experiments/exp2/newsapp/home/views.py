from django.shortcuts import render
from .models import StudentNews, FacultyNews, EventsNews

# Create your views here.
def home(request):
    student_news = StudentNews.objects.latest('sno')
    faculty_news = FacultyNews.objects.latest('sno')
    events_news = EventsNews.objects.latest('sno')
    return render(request, 'home.html', {'student_news': student_news, 'faculty_news': faculty_news, 'events_news': events_news})

def student(request):
    student_news = StudentNews.objects.all()
    return render(request, 'student.html', {'student_news': student_news})
    
def faculty(request):
    faculty_news = FacultyNews.objects.all()
    return render(request, 'faculty.html', {'faculty_news': faculty_news})
    
def events(request):
    events_news = EventsNews.objects.all()
    return render(request, 'events.html', {'events_news': events_news})

def news(request, id, category):
    if category == 'student':
        news = StudentNews.objects.filter(sno=id)
    elif category == 'faculty':
        news = FacultyNews.objects.filter(sno=id)
    elif category == 'events':
        news = EventsNews.objects.filter(sno=id)
    return render(request, 'news.html', {'news': news[0]})