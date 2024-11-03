from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import *
from .models import *
from datetime import datetime,date
from appointment.models import *

# Create your views here.
@login_required(login_url='/login/')
def patient_db(request,chosenfield):
  sidefields= ['User Profile', 'Members', 'Appointments']
  context= {
    'sidefields': sidefields,
    'chosenfield': chosenfield,
    'userInfo': UserInfo.objects.filter(user= request.user)[0],
    'patients': Patient.objects.filter(user= request.user).order_by('first_name','last_name'),
    'appointments': Appointment.objects.filter(patient__user= request.user).order_by('-date')
  }
  # if not request.GET.get('fieldselected') == None:
  #   information=request.GET
  #   chosenfield=int(information.get('fieldselected')[0])
  #   context['chosenfield']= chosenfield
  #   templte="field"+chr(chosenfield + 48)+".html"
  #   return render(request, templte, context)
  
  templte="field"+chr(chosenfield + 48)+".html"
  return render(request, templte, context)

@login_required(login_url='/login/')
def addapatient(request):

  if request.method== 'POST':
    information= request.POST
    user= request.user
    first_name= information.get('first_name')
    last_name= information.get('last_name')
    dob= (datetime.strptime(information.get('dob'), "%Y-%m-%d")).date()
    sex= information.get('sex')

    if dob > date.today():
      messages.error(request, "Date of Birth is in future")
      return redirect('/addapatient/')

    patient=Patient.objects.create(
      user= user,
      first_name= first_name,
      last_name= last_name,
      dob= dob,
      sex= sex,
    )
    patient.save()

    if request.GET.get('next') != None:
      return redirect(request.GET.get('next'))  
    return redirect('patient_db',2)

  return render(request, 'addapatient.html')

def doctorsnote(request,apt_id):
  appointment=Appointment.objects.filter(id=apt_id).first()
  context={
    'name': appointment.patient.first_name+' '+appointment.patient.last_name,
    'doctor': appointment.slot.doctor.user.first_name+' '+appointment.slot.doctor.user.last_name,
    'dateandtime': (appointment.date).strftime('%d %B %Y | %A'),
    'note': appointment.doctorsnote,
    'tests': appointment.test.all,
  }
  return render(request,'doctornote.html',context)