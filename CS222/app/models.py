from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 150, null = True)
    major = models.CharField(max_length = 150, null = True)
    hobbies = models.CharField(max_length = 300, null = True)
    classes = models.CharField(max_length = 150, null = True)
    social_media = models.CharField(max_length = 300, null = True)
    email = models.CharField(max_length = 300, null = True)

    def __str__(self):
        return self.email + ' ' + self.major + ' ' + self.hobbies + ' ' + self.classes + ' ' + self.social_media