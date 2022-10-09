from django.db import models
from django.contrib.auth.models import User

class Regist(models.Model):
    username = models.CharField(max_length=50,default=None)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    password = models.CharField(max_length=100,default=None)
    password2 = models.CharField(max_length=100,default=None)


