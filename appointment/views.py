from django.shortcuts import render, redirect
from doctor.models import Doctor, AppointmentSlot
from patient.models import *
from .models import *
from collections import OrderedDict, defaultdict
from datetime import datetime, date,timedelta
from django.contrib import messages
from account.models import *
from .forms import *
# Create your views here.

def order_availability(data):
    # Get today's day name and find the next day (tomorrow)
    today = datetime.now().strftime('%A').upper()
    weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    tomorrow_index = (weekdays.index(today) + 1) % 7
    ordered_weekdays = weekdays[tomorrow_index:] + weekdays[:tomorrow_index]

    # Time of day order
    time_order = ['MORNING', 'AFTERNOON', 'EVENING']
    today_date= date.today()
    # Sort the dictionary based on ordered weekdays and time of day
    sorted_data = OrderedDict()

    for count, day in enumerate(ordered_weekdays):
        if day in data:
            # Sort inner dictionary by time of day order
            sorted_inner = OrderedDict(sorted(data[day].items(), key=lambda x: time_order.index(x[0])))
            key= day+" | "+((today_date+timedelta(days=count+1)).strftime('%d %m %Y'))
            sorted_data[key] = sorted_inner

    # Display the ordered dictionary
    return sorted_data

def tuple_formatting(list_tuple):
    # Initialize a defaultdict with list as the default factory
    result = {}
    today= date.today()
    # Iterate over each tuple
    for key, value, id in list_tuple:
        if key not in result:
            result[key] = {}
        current=Appointment.objects.filter(slot__id=id,date__gt=today).count()
        maxim=AppointmentSlot.objects.filter(id=id).first().max_bookings
        avail= current<maxim
        result[key][value]={'id':id,'available':avail}

    # Convert back to a regular dictionary (optional)
    # result = dict(result)
    return result

def finddate(day):
    weekdays = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    date_today= date.today()
    today_no= date_today.weekday()
    day_no= weekdays.index(day)
    print(today_no)
    print(day)
    print(day_no)
    delta= day_no-today_no
    if delta <= 0:
        delta=7+delta
    print(delta)
    required_date= date_today+timedelta(days=delta)
    return required_date
    

def book_appointment(request, doctor_id):
    # Get all doctors for the initial selection
    doctor= Doctor.objects.filter(id= doctor_id).first()
    availability= AppointmentSlot.objects.filter(doctor= doctor).values_list('day_of_week','session','id')
    doctor= doctor.user
    doctor= doctor.first_name+' '+doctor.last_name
    members= Patient.objects.filter(user=request.user)
    
    slots_assigned=tuple_formatting(availability) 
    slots_assigned= order_availability(slots_assigned)

    # print(slots_assigned)
    context = {'doctor': doctor,
               'members': members,
               'doctor_id': doctor_id,
               'sorted_data': slots_assigned
              }
    
    if request.method == 'POST':
        information= request.POST
        patient_id= information.get('patient_id')
        slot_id= information.get('slot_id')

        if patient_id == '':
            messages.error(request, "Select a member")
            return redirect('book_appointment',doctor_id=doctor_id)
        
        if slot_id == '':
            messages.error(request, "Select an available slot")
            return redirect('book_appointment',doctor_id=doctor_id)
        
        
        aptdate= finddate(AppointmentSlot.objects.filter(id=slot_id).first().day_of_week)
        appointment= Appointment.objects.create(
            patient= Patient.objects.filter(id=patient_id).first(),
            date= aptdate,
            slot= AppointmentSlot.objects.filter(id= slot_id).first()
        )
        appointment.save()
        messages.success(request,"Appointment Booked for "+aptdate.strftime('%d %B %Y'))
        return redirect('home')
    
    return render(request, 'book_appointment.html', context)

def update_feedback(request,pk):
    appointment = Appointment.objects.filter(id=pk).first()
    form =FeedbackForm(instance=appointment)
    if request.method =="POST":
        form = FeedbackForm(request.POST,instance=appointment)
        if form.is_valid():
            form.save()
            patient = appointment.patient
            return redirect('patient_db')


    context={'form':form}
    return render(request,'update_feedback.html',context)

def cancelappointment(request, apt_id):
    appointment=Appointment.objects.filter(id=apt_id).first()
    appointment.stat='CANCELLED'
    appointment.save()

    role=UserInfo.objects.filter(user=request.user).first().role_def

    if role == 'DOCTOR':
        pk=Doctor.objects.filter(user=request.user).first().id
        return redirect('doctor-dashboard',pk=pk)
    
    return redirect('patient_db')

def completeappointment(request, apt_id):
    appointment=Appointment.objects.filter(id=apt_id).first()
    appointment.stat='COMPLETED'
    appointment.save()
    pk=appointment.slot.doctor.id
    return redirect('doctor-dashboard',pk=pk)