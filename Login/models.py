from django.db import models
from django.contrib.auth.models import AbstractUser

class Employee(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)

class Patient(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
