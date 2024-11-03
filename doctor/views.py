from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from doctor.models import *
from appointment.models import *
from django.db.models import Q
from .forms import *
from datetime import date
from collections import OrderedDict
from hospital_test.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from hmes.decorator import *

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

@login_required(login_url='login_page')
@role_required(['DOCTOR'])
def doctor_dashboard(request,pk):
    doctor=Doctor.objects.get(id=pk)
    appointments = Appointment.objects.filter(slot__doctor=doctor, date=date.today(), stat= 'CONFIRMED').order_by('-date')
    tests = Test.objects.all()
    if request.method == "POST":
        appointment_id = request.POST.get('appointment_id')
        appointment = Appointment.objects.filter(id=appointment_id).first()
        if request.POST.get('doctor_note') is not None:
           
            appointment.doctorsnote = request.POST.get('doctor_note')
            appointment.save()

        elif request.POST.get('test') is not None:
                test_name = request.POST.get('test').strip()  
                test = Test.objects.filter(name=test_name).first()
                if test:
                    appointment.test.add(test)
                    messages.success(request, "Test Added!")
                else:
                    messages.error(request, "Test not available!")

        return redirect('doctor-dashboard', pk=doctor.id)
    context={'doctor':doctor,'appointments':appointments,'tests':tests}
    return render(request,'doctor_dashboard.html',context)

def tuple_formatting(tuple_list):
    result={}
    for key,value in tuple_list:
        if key not in result:
            result[key]=[]
        result[key].append(value)
    
    # Desired order of days and times
    day_order = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    time_order = {'MORNING': 1, 'AFTERNOON': 2, 'EVENING': 3}

    # Arrange the dictionary according to the specified order
    sorted_availability = OrderedDict(
        (day, sorted(result[day], key=lambda time: time_order[time]))
        for day in day_order if day in result
    )

    return sorted_availability

def doctor_profile(request,pk):
    doctor=Doctor.objects.get(id=int(pk))

    availability = AppointmentSlot.objects.filter(doctor=doctor).values_list('day_of_week', 'session')
    availability = tuple_formatting(availability)
    
    context={'doctor':doctor, 'availability':availability}
    return render(request,'doctor_profile.html',context)

@login_required(login_url='login_page')
@role_required(['DOCTOR'])
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

@login_required(login_url='login_page')
@role_required(['DOCTOR'])
def appointment_overview(request,pk):
    q=request.GET.get('q') if (request.GET.get('q')!=None) else ''
    doctor=Doctor.objects.get(id=pk)
    tests = Test.objects.all()
    appointments = Appointment.objects.filter(slot__doctor=doctor,stat__icontains=q)
    appointment_cancelled = Appointment.objects.filter(slot__doctor=doctor,stat='CANCELLED').count()
    appointment_confirmed = Appointment.objects.filter(slot__doctor=doctor,stat='CONFIRMED').count()
    appointment_completed = Appointment.objects.filter(slot__doctor=doctor,stat='COMPLETED').count()
    appointment_total=Appointment.objects.filter(slot__doctor=doctor).count()
    context={'appointments':appointments,'doctor':doctor,'test':tests,'appointment_cancelled':appointment_cancelled,'appointment_confirmed':appointment_confirmed,'appointment_completed':appointment_completed,'appointment_total':appointment_total}
    return render(request,'appointment_overview.html',context)

@login_required(login_url='login_page')
@role_required(['DOCTOR'])
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

@login_required(login_url='login_page')
@role_required(['DOCTOR','STAFF'])
def doctor_feedback(request,pk):
    doctor = Doctor.objects.filter(id=pk).first()
    appointments = Appointment.objects.filter(slot__doctor = doctor ).exclude(feedback = None)
    context={'appointments':appointments,'doctor':doctor}
    return render(request,'feedback_page.html',context)

@login_required(login_url='login_page')
@role_required(['DOCTOR'])
def confirmation(request,pk):
    appointment = Appointment.objects.get(id=int(pk))
    doctor = appointment.slot.doctor
    str=request.GET.get('q')
    context={'str':str,'appointment':appointment,'doctor':doctor}
    return render(request,'confirmation.html',context)