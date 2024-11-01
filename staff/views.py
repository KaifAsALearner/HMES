# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from doctor.models import *

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
        return redirect(reverse('doctor_availability', args=[doctor_id]))

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
