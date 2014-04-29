'''
Created on Apr 27, 2014

@author: Duy Tran
'''
from django.db import models
from django.contrib.auth.models import User

class People(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)