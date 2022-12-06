"""NetworkEZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views as v


# Urls for the views.py 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('app/', include('django.contrib.auth.urls')),
    path('register/', v.register, name="register"),
    path('login/', v.loginPage, name="login"),
    path('home/', v.home, name="home"),
    path('logout/', v.logoutUser, name="logout"),
    path('profiles/', v.studentProfile, name="profiles"),
    path('filtered_profiles/', v.filterStudentProfile, name= "filtered_profiles"),
    path('filtered_hobbies/', v.filterStudentHobbies, name= "filtered_hobbies"),
    path('your_profile/', v.your_profile, name= "your_profile")

]
