# forms.py file that initalizes the forms for registration, a user student form, and a form for the rest of the students
# Comprises of CreateUserForm, StudentForm, UserForm

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student, UserStudent
from django import forms

# Creates the UserForm needed for registration
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Creates the StudentForm that stores all the other student's data
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'major', 'hobbies', 'classes', 'social_media', 'email']
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'major': forms.TextInput(attrs={'class': 'form-control'}),
            'hobbies': forms.TextInput(attrs={'class': 'form-control'}),
            'classes': forms.TextInput(attrs={'class': 'form-control'}),
            'social_media': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),

        }

# Creates the UserForm that stores all the current user's data
class UserForm(forms.ModelForm):
    class Meta:
        model = UserStudent
        fields = ['name', 'major', 'hobbies', 'classes', 'social_media', 'email']
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'major': forms.TextInput(attrs={'class': 'form-control'}),
            'hobbies': forms.TextInput(attrs={'class': 'form-control'}),
            'classes': forms.TextInput(attrs={'class': 'form-control'}),
            'social_media': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),

        }
