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