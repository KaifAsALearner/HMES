from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from account.models import *
from doctor.models import *

# Create your views here.
def home(request):
  return render(request,'homepage.html')

@login_required(login_url='/login/')
def dashboard(request):
  role= UserInfo.objects.filter(user = request.user)[0].role_def
  if role == 'PATIENT':
    return redirect('patient_db')
  elif role == 'DOCTOR':
    doctor= Doctor.objects.filter(user=request.user).first()
    return redirect('doctor-dashboard',pk=doctor.id)
  else :
    return redirect('/')