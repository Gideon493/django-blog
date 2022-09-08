from datetime import datetime
from email.policy import default
from tkinter import CASCADE
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User


class Members(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    dob = models.DateField(default=datetime.now)
    idnumber = models.IntegerField(null=True)
    photo = models.ImageField(default='default.jpg', blank=True)

# Create your models here.

    def __str__(self):
        return self.firstname

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    photo = models.ImageField(default = 'default.jpg')
    author = models.ForeignKey(User,default=None, on_delete = models.CASCADE)
    
    
    def __str__(self):
        return self.title   
