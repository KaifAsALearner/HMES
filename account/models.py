from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#1
class UserInfo(models.Model):
  user= models.OneToOneField(User, on_delete= models.CASCADE)
  mobile_number= models.BigIntegerField(unique= True)
  role_def= models.CharField(max_length= 20, choices=[('DOCTOR', 'Doctor'), ('PATIENT', 'Patient'), ('STAFF', 'Staff')], default= 'PATIENT')

  def __str__(self) -> str:
    return self.user.username
  
  class Meta:
    verbose_name = ("user")

#2
class Patient(models.Model):
  user_info= models.ForeignKey(UserInfo, on_delete= models.CASCADE)
  first_name= models.CharField(max_length= 255)
  last_name= models.CharField(max_length= 255, blank= True, null= True)
  dob= models.DateField(default= None)
  sex= models.CharField(max_length= 10, choices= [('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], default= 'FEMALE')

#3
class Doctor(models.Model):
  user_info= models.OneToOneField(UserInfo, on_delete= models.CASCADE)
  dob= models.DateField(default= None)
  sex= models.CharField(max_length= 10, choices= [('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], default= 'FEMALE')
  specialization = models.CharField(max_length=255, default= None)
  availability = models.CharField(max_length=10, choices= [('YES', 'Yes'), ('NO', 'No')], default= 'YES')