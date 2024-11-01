from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import *
from .models import *
from datetime import datetime,date

# Create your views here.
@login_required(login_url='/login/')
def patient_db(request):
  sidefields= ['User Profile', 'Patients', 'Appointments']
  chosenfield= 1
  context= {
    'sidefields': sidefields,
    'chosenfield': 1,
    'userInfo': UserInfo.objects.filter(user= request.user)[0],
    'patients': Patient.objects.filter(user= request.user).order_by('first_name','last_name')
  }
  if not request.GET.get('fieldselected') == None:
    information=request.GET
    chosenfield=int(information.get('fieldselected')[0])
    context['chosenfield']= chosenfield
    templte="field"+chr(chosenfield + 48)+".html"
    return render(request, templte, context)
  
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
    return redirect('/dashboard/p/')

  return render(request, 'addapatient.html')