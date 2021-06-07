from django.db import models

# Create your models here.

class user(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)

def __str__(self):
    return user.content