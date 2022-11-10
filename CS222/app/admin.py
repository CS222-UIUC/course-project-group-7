from django.contrib import admin

# Register your models here.
from .models import Student, UserStudent

admin.site.register(Student)
admin.site.register(UserStudent)
