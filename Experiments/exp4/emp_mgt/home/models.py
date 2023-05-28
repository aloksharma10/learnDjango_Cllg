from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Role(models.Model):
    name=models.CharField(max_length=50)
    dept= models.ForeignKey(Department, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Employee(models.Model):
    eno=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=50)
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    img= models.ImageField(upload_to='static/assets/img',default="")
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    dept= models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

