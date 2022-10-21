from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register(response):
    if response.method == "POST":
        form = CreateUserForm(response.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(response, "Account was registered successfully for " + user)
            return redirect('login')
        
    else:
        form =  CreateUserForm()

    return render(response, 'register/register.html', {"form" : form})

def loginPage(request):
    error = False
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = authenticate(request, username = username, password = password)

        if username == '':
            messages.info(request, 'Username is required')
            error = True
        if password == '':
            messages.info(request, 'Password is required')
            error = True
        if user is not None and error == False:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            error = True

    context = {}
    if error:
        return render(request, 'register/login.html', status = 401, context = context)
    return render(request, 'register/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
def home(request):
    return render(request, 'register/dashboard.html', {})