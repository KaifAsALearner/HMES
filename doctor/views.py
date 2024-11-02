from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from doctor.models import *
from appointment.models import *
from django.db.models import Q
from .forms import *
from django.utils import timezone
from datetime import date

# Create your views here.
def doctor(request):
    q=request.GET.get('q') if (request.GET.get('q')!=None) else ''
    doctors=Doctor.objects.filter(
        Q(department__dept_name__icontains=q) |
        Q(user__first_name__icontains=q) |
        Q(user__last_name__icontains=q)
    ).distinct()
    
    departments=Department.objects.all()
    context={'departments':departments, 'doctors':doctors, 'field': 0}
    if not q == '' and request.GET.get('i') != None:
        context['field']=int(request.GET.get('i'))
    return render(request,'doctor_page.html',context)


def doctor_dashboard(request,pk):
    doctor=Doctor.objects.get(id=pk)
    appointments = Appointment.objects.filter(slot__doctor=doctor, date=date.today()).order_by('date')
    if request.method == "POST":
        appointment_id = request.POST.get('appointment_id')
        appointment = Appointment.objects.filter(id = appointment_id).first()
        appointment.doctorsnote = request.POST.get('doctor_note')
        appointment.save()
        return redirect('doctor-dashboard',pk=doctor.id)
    context={'doctor':doctor,'appointments':appointments}
    return render(request,'doctor_dashboard.html',context)

def doctor_profile(request,pk):
    doctor=Doctor.objects.get(id=int(pk))
    context={'doctor':doctor}
    return render(request,'doctor_profile.html',context)

def doctor_update(request,pk):
    doctor=Doctor.objects.get(id=int(pk))
    form = DoctorForm(instance=doctor)
    if (request.method=='POST'):
        form = DoctorForm(request.POST,request.FILES,instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor-profile',pk=doctor.id)
       
    context={'form':form}
    return render(request,'doctor_update.html',context)

def appointment_overview(request,pk):
    doctor=Doctor.objects.get(id=pk)
    appointments = Appointment.objects.filter(slot__doctor=doctor).order_by('date')
    context={'appointments':appointments,'doctor':doctor}
    return render(request,'appointment_overview.html',context)

def doctor_note(request,pk):
    appointment = Appointment.objects.get(id=int(pk))
    form = NoteForm(instance=appointment)
    if request.method == "POST":
        form = NoteForm(request.POST,instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('doctor-dashboard',pk=appointment.slot.doctor.id)
    context={'form':form}
    return render(request,'doctor_note.html',context)