from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *


# Create your views here.
#login_page
def login_page(request):

  if request.method == "POST":
    information= request.POST
    user_name= information.get('user_name')

    if not User.objects.filter(username= user_name).exists():

      if user_name.isdigit() and UserInfo.objects.filter(mobile_number= user_name).exists():
        user_name=UserInfo.objects.filter(mobile_number= user_name)[0].user.username

      else:
        messages.error(request, "Invalid Username/ Mobile Number")
        return redirect('/login/')
    
    password= information.get('password')
    user= authenticate(username= user_name, password= password)

    if user is None:
      messages.error(request, "Incorrect Password")
      return redirect('/login/')
    
    else:
      login(request, user)
      messages.success(request, "Logged in successfully")
      return redirect('/')

  return render(request,'loginpage.html')

#logout_page
@login_required(login_url='login_page')
def logout_page(request):
  logout(request)
  return redirect('/')

#register_page
def register_page(request):

  if request.method == "POST":
    information=request.POST
    user_name=information.get('user_name')
    phone_number= information.get('phone_number')
    email= information.get('email') 

    if User.objects.filter(username= user_name).exists():
      messages.error(request, "Username already taken")
      return redirect('/register/')
    
    if UserInfo.objects.filter(mobile_number= phone_number).exists():
      messages.error(request, "Phone number already linked to an account")
      return redirect('/register/')
    
    if User.objects.filter(email= email).exists():
      messages.error(request, "Email already linked to an account")
      return redirect('/register/')

    first_name= information.get('first_name')
    last_name= information.get('last_name') 
    password= information.get('password')

    user=User.objects.create(
      username= user_name,
      first_name= first_name,
      last_name= last_name,
      email= email,
    )
    user.set_password(password)
    user.save()

    userinfo= UserInfo.objects.create(
      user= user,
      mobile_number= phone_number,
    )
    userinfo.save()
    login(request, authenticate(username= user_name, password= password))
    messages.success(request, "Account created successfully")
    return redirect('/')


  return render(request,'registerpage.html')