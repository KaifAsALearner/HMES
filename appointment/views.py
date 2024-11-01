
from django.shortcuts import render, get_object_or_404
from doctor.models import Doctor, AppointmentSlot
from patient.models import *
from collections import OrderedDict, defaultdict
from datetime import datetime
# Create your views here.

def order_availability(availability_dict):
    # Define the weekday order starting from today
    weekday_order = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    today_index = datetime.today().weekday()  # Get the current weekday index (0=Monday, 6=Sunday)
    
    # Create a custom ordered list of days starting from today
    ordered_days = weekday_order[today_index + 1:] + weekday_order[:today_index + 1]
    
    # Define the order of time slots
    time_order = ['MORNING', 'AFTERNOON', 'EVENING']
    
    # Create a new ordered dictionary for the sorted result
    sorted_availability = OrderedDict()
    
    # Sort the keys based on the custom weekday order
    for day in ordered_days:
        if day in availability_dict:
            # Sort the values (time of day) and keep only valid options
            sorted_times = sorted(set(availability_dict[day]), key=lambda x: time_order.index(x))
            if sorted_times:
                sorted_availability[day] = sorted_times

    return sorted_availability

def tuples_to_dict(list_tuple):
    # Initialize a defaultdict with list as the default factory
    result = defaultdict(list)

    # Iterate over each tuple
    for key, value in list_tuple:
        result[key].append(value)

    # Convert back to a regular dictionary (optional)
    result = dict(result)
    return result

def book_appointment(request, doctor_id):
    # Get all doctors for the initial selection
    doctor= Doctor.objects.filter(id= doctor_id).first()
    availability= AppointmentSlot.objects.filter(doctor= doctor).values_list('day_of_week','session')
    doctor= doctor.user
    doctor= doctor.first_name+' '+doctor.last_name
    members= Patient.objects.filter(user=request.user)
    
    slots_assigned=tuples_to_dict(availability) 
    slots_assigned= order_availability(slots_assigned)

    context = {'doctor': doctor,
               'doctor_id': doctor_id,
               'members': members,
               'slots': slots_assigned}
    
    return render(request, 'book_appointment.html', context)
