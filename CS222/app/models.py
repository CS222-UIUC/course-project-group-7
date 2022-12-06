# models.py file that creates the model needed for the database
from django.db import models

# Creates Student Models
class Student(models.Model):
    name = models.CharField(max_length=150, null=True)
    major = models.CharField(max_length=150, null=True)
    hobbies = models.CharField(max_length=300, null=True)
    classes = models.CharField(max_length=150, null=True)
    social_media = models.CharField(max_length=300, null=True)
    email = models.CharField(max_length=300, null=True)

# Creates Current User Models
class UserStudent(models.Model):
    name = models.CharField(max_length=150, null=True)
    major = models.CharField(max_length=150, null=True)
    hobbies = models.CharField(max_length=300, null=True)
    classes = models.CharField(max_length=150, null=True)
    social_media = models.CharField(max_length=300, null=True)
    email = models.CharField(max_length=300, null=True)
