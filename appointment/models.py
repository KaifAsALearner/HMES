from django.db import models
from doctor.models import *
from patient.models import *
from hospital_test.models import *
from auditlog.registry import auditlog
# Create your models here.


#1
class Appointment(models.Model):
  patient= models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
  date = models.DateField(null=True, blank=True)
  slot= models.ForeignKey(AppointmentSlot, on_delete= models.CASCADE)
  stat= models.CharField(max_length= 20, choices=[('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Cancelled'), ('COMPLETED','Completed')], default= 'CONFIRMED')
  booking_time= models.DateTimeField(auto_now=True)
  feedback= models.TextField(blank=True,null=True)
  test= models.ManyToManyField(Test,blank=True)
  doctorsnote= models.TextField(default='',blank=True,null=True)

  def __str__(self) -> str:
    return f'User: {self.patient.user.first_name} {self.patient.user.first_name} | Doctor: {self.slot.doctor.user.first_name} {self.slot.doctor.user.last_name}'


auditlog.register(Appointment)