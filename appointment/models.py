from django.db import models
from doctor.models import *
from patient.models import *
# Create your models here.


#1
class Appointment(models.Model):
  patient= models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
  date = models.DateField(null=True, blank=True)
  slot= models.ForeignKey(AppointmentSlot, on_delete= models.CASCADE)
  stat= models.CharField(max_length= 20, choices=[('CONFIRMED', 'Confirmed'), ('CANCELLED', 'Cancelled'), ('COMPLETED','Completed')], default= 'CONFIRMED')
  paid= models.CharField(max_length= 5, choices=[('YES', 'Yes'), ('NO','No')],default='NO')
  booking_time= models.DateTimeField(auto_now=True)
  feedback= models.TextField(blank=True,null=True)
  # test= models.ManyToManyField()
  doctorsnote= models.TextField(default='',blank=True,null=True)