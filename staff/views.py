# views.py
from django.shortcuts import render, get_object_or_404, redirect
from doctor.models import *
from appointment.models import *
from django.contrib.auth.decorators import login_required
from account.models import *
from datetime import date
from hospital_test.models import *
from .forms import *
from hmes.decorator import *
from auditlog.models import LogEntry

@login_required(login_url='login_page')
@role_required(['STAFF'])
def doctor_availability(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    sessions = ['MORNING', 'AFTERNOON', 'EVENING']

    # Handle form submission to update availability
    if request.method == 'POST':
        # Clear all slots for this doctor before updating, to reset any unchecked boxes
        AppointmentSlot.objects.filter(doctor=doctor).delete()

        # Add selected slots
        for day in days:
            for session in sessions:
                session_name = f"{day}_{session}"
                if request.POST.get(session_name):
                    # Save or update availability in the AppointmentSlot model
                    AppointmentSlot.objects.create(doctor=doctor, day_of_week=day, session=session)

        # Redirect to the same page to refresh with updated data
        return redirect('staff_db',2)

    # Get all available appointment slots for the doctor
    available_slots = AppointmentSlot.objects.filter(doctor=doctor).values_list('day_of_week', 'session')
    
    # Preformat the availability keys as "DAY_SLOT" (e.g., "MONDAY_MORNING")
    available_slots_set = {f"{day}_{session}" for day, session in available_slots}

    context = {
        'doctor': doctor,
        'days': days,
        'sessions': sessions,
        'available_slots': available_slots_set,
    }
    
    return render(request, 'doctor_availability.html', context)


def builddoctors(doctorstuple):
    doctors=[]
    today= date.today()
    for id,fn,ln in doctorstuple:
        single={}
        single['id']=id
        single['first_name']=fn
        single['last_name']=ln
        previous=Appointment.objects.filter(slot__doctor__id=id, date__lt= today, stat='COMPLETED').count()
        upcoming=Appointment.objects.filter(slot__doctor__id=id, date__gt= today).exclude(stat='CANCELLED').count()
        todays=Appointment.objects.filter(slot__doctor__id=id, date= today).exclude(stat='CANCELLED').count()
        single['prev']=previous
        single['upco']=upcoming
        single['toda']=todays
        doctors.append(single)
    
    return doctors


@login_required(login_url='login_page')
@role_required(['STAFF'])
def staff_db(request,chosenfield):
    sidefields= ['User Profile', 'Doctors', 'Appointments','Tests','Audit']
    doctors= Doctor.objects.all().values_list('id','user__first_name','user__last_name')
    doctors=builddoctors(doctors)
    context= {
    'sidefields': sidefields,
    'chosenfield': chosenfield,
    'userInfo': UserInfo.objects.filter(user= request.user)[0],
    'doctors':doctors,
    'appointments':Appointment.objects.all(),
    'currentdoc':'All',
    'tests': Test.objects.all(),
    'logs': LogEntry.objects.all().order_by('-timestamp'),
    }
    if request.GET and chosenfield == 3 :
        information=request.GET
        doctor_id=information.get('doctor_id')
        if doctor_id == '':
            context['currentdoc']='All'
            context['appointments']=Appointment.objects.all()
        else:
            context['currentdoc']=information.get('doctor')
            context['appointments']=Appointment.objects.filter(slot__doctor__id=doctor_id)

    if request.GET and chosenfield == 5 :
        context['logs']= LogEntry.objects.all().order_by('-timestamp')

    templte="staff"+chr(chosenfield + 48)+".html"
    return render(request, templte, context)

@login_required(login_url='login_page')
@role_required(['STAFF'])
def update_test(request,test_id):
    test=Test.objects.filter(id=test_id).first()
    form=TestForm(instance=test)

    if request.method =="POST":
        form = TestForm(request.POST,instance=test)
        if form.is_valid():
            form.save()
            return redirect('staff_db',4)
    
    context={'form':form}
    return render(request,'update_test.html',context)

@login_required(login_url='login_page')
@role_required(['STAFF'])
def addatest(request):

  if request.method== 'POST':
    information= request.POST
    name= information.get('name')
    descript= information.get('descript')

    test=Test.objects.create(
        name=name,
        descript=descript,
    )
    test.save()
    return redirect('staff_db',4)

  return render(request, 'addatest.html')