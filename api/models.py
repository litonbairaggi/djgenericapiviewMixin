from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=64, blank=False, default='')
    email = models.EmailField(max_length=64,blank=False, default='')
    city = models.CharField(max_length=64, blank=False, default='')
    createdat = models.DateTimeField(auto_now_add=True)