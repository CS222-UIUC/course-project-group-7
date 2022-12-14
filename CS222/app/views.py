# Views.py file that is used to connect the backend with the front-end
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm
from .forms import StudentForm, UserForm
from .models import Student, UserStudent


# Checks to see if there is a post request and registers a username and password if there is one
def register(response):
    if response.method == "POST":
        form = CreateUserForm(response.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(response, "Account was registered successfully for " + user)
            return redirect('login')
    else:
        form = CreateUserForm()

    return render(response, 'register/register.html', {"form": form})

# Authenticates the user to be logged in if the username and password are valid 
def loginPage(request):
    error = False
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if username == '':
            messages.info(request, 'Username is required')
            error = True
        if password == '':
            messages.info(request, 'Password is required')
            error = True
        if user is not None and error is False:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            error = True

    context = {}
    if error:
        return render(request, 'register/login.html', status=401, context=context)
    return render(request, 'register/login.html', context)


# Logout the current user 
def logoutUser(request):
    logout(request)
    return redirect('login')

# Directs the user to the home page
def home(response):
    if response.method == "POST":
        form = StudentForm(response.POST)
        userForm = UserForm(response.POST)
        if form.is_valid:
            form.save()
            userForm.save()
            return redirect('profiles')
    else:
        form = StudentForm()

    return render(response, 'register/dashboard.html', {"form": form})

# Shows the all of the profile's in the database
def studentProfile(response):
    student_list = Student.objects.all()
    return render(response, 'register/student_profile.html', {'student_list': student_list})

# Filtering used to find student's with the similar classes
def filterStudentProfile(response):
    student_list = Student.objects.all()

    user_list = UserStudent.objects.all()

    match_class = user_list[0].classes.split(",")
    temp = []
    for student in student_list:
        for class_ in match_class:
            if class_.strip().upper() in student.classes:
                temp.append(student)
                break

    return render(response, 'register/filtered_profiles.html', {'student_list': temp})

# Filtering used to find student's with the similar hobbies
def filterStudentHobbies(response):
    student_list = Student.objects.all()
    user_list = UserStudent.objects.all()

    match_hobbie = user_list[0].hobbies.split(",")
    temp = []
    for student in student_list:
        for hobbie in match_hobbie:
            if hobbie.strip().lower() in student.hobbies:
                temp.append(student)
                break

    return render(response, 'register/filtered_hobbies.html', {'student_list': temp})

# Shows your own profile 
def your_profile(response):
    user_list = UserStudent.objects.all()

    return render(response, 'register/your_profile.html', {'student_list': user_list})
