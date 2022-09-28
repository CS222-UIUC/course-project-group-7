import email
from django.db import models

class Student(models.Model):
    email = models.CharField(max_length = 150, null = True)
    password = models.CharField(max_length = 150, null = True)
    full_name = models.CharField(max_length = 150, null = True)
    major = models.CharField(max_length = 150, null = True)
    hobbies = models.CharField(max_length = 300, null = True)
    classes = models.CharField(max_length = 150, null = True)
    social_media = models.CharField(max_length = 300, null = True)