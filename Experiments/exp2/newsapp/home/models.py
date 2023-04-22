from django.db import models

# Create your models here.
class StudentNews(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    action=models.TextField(default="")
    desc=models.TextField()
    result=models.TextField(default="")
    img= models.ImageField(upload_to='static/postImg',default="")
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

class FacultyNews(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    action=models.TextField(default="")
    desc=models.TextField()
    result=models.TextField(default="")
    img= models.ImageField(upload_to='static/postImg',default="")
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.title

class EventsNews(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    action=models.TextField(default="")
    desc=models.TextField()
    result=models.TextField(default="")
    img= models.ImageField(upload_to='static/postImg',default="")
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.title
