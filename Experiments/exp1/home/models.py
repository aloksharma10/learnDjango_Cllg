from django.db import models

# Added manually
class User(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
       
    def __str__(self):
        return self.name

class Emp(models.Model):
    sno = models.AutoField(primary_key=True)
    Ename = models.CharField(max_length=255)
    Eemail = models.CharField(max_length=255)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
       
    def __str__(self):
        return self.Ename

class Product(models.Model):
    sno = models.AutoField(primary_key=True)
    Productname = models.CharField(max_length=255)
    Slug = models.CharField(max_length=255)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
       
    def __str__(self):
        return self.Productname

