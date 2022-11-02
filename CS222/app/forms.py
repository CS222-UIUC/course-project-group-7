# from django.forms import ModelForm, forms
# from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Student
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'major', 'hobbies', 'classes', 'social_media', 'email']
        widget = {
            'name' : forms.TextInput(attrs= {'class' : 'form-control'}),
            'major' : forms.TextInput(attrs= {'class' : 'form-control'}),
            'hobbies' : forms.TextInput(attrs= {'class' : 'form-control'}),
            'classes' : forms.TextInput(attrs= {'class' : 'form-control'}),
            'social_media' : forms.TextInput(attrs= {'class' : 'form-control'}),
            'email' : forms.TextInput(attrs= {'class' : 'form-control'}),

        }
