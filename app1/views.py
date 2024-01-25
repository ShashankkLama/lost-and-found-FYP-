from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from django.contrib.auth import logout



# views here.
@login_required(login_url='login')
def HomePage(request):
    if request.user:
        print(request.user)
        return render(request, 'home.html')
    else:
        return redirect('/ ')
    

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse("Your passwords donot match, try again.")
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            
            return redirect('login')
        print(uname, email, pass1, pass2)
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':  
        username=request.POST.get('username')
        pass1= request.POST.get('pass')
        print(username, pass1)
        
        user=authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('home')
        else:
            return redirect('/')
        
        
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')