from django.contrib import admin
from . models import StudentNews,FacultyNews,EventsNews
# Register your models here.
admin.site.register(StudentNews)
admin.site.register(FacultyNews)
admin.site.register(EventsNews)