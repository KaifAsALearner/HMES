from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime,date
from .models import *

# Create your views here.
def bookanappt(request):
  members= Patient.objects.filter(user= request.user).values_list('first_name','last_name')
  members = [f"{first} {last}" for first, last in members]
  doctors= Doctor.objects.values_list('user__first_name','user__last_name')
  doctors = [f"{first} {last}" for first, last in doctors]
  context={
    'members': members,
    'doctors': doctors,
  }

  if request.method == 'POST':
    information= request.POST
    member=information.get('member')
    doctor=information.get('doctor')
    aptdate= information.get('aptdate')
    # aptdate= (datetime.strptime(information.get('aptdate'), "%Y-%m-%d")).date()

    if member == '' or doctor == '' or aptdate == '':
      messages.error(request, "Fill in the details correctly")
      return redirect('bookanappt')
    
    aptdate= (datetime.strptime(aptdate, "%Y-%m-%d")).date()

    if aptdate <= date.today():
      messages.error(request, "Appointment cannot be booked at this date")
      return redirect('bookanappt')
    
    print(Patient.objects.filter(user=request.user, ))
    # appointment=Appointment.objects.create(
    #   user= user,
    #   first_name= first_name,
    #   last_name= last_name,
    #   dob= dob,
    #   sex= sex,
    # )
    # appointment.save()

  return render(request, 'bookanappt.html', context)
