from django.db import models

# Create your models here.
class Test(models.Model):
    eno=models.IntegerField()
    name=models.CharField(max_length=65)