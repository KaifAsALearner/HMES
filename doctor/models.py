from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    dept_name=models.CharField(max_length=200)

    def __str__(self):
        return self.dept_name
    
    class Meta:
       ordering = ['dept_name']  # Ascending order by hire_date

    

class Doctor(models.Model):
  user= models.OneToOneField(User, on_delete= models.CASCADE,default=1)
  dob= models.DateField(default= None)
  sex= models.CharField(max_length= 10, choices= [('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], default= 'FEMALE')
  department = models.ManyToManyField(Department)
  specialization = models.TextField(blank= True, null= True)
  dayofstarting= models.DateField(auto_now= True)
  def __str__(self):
    return self.user.first_name