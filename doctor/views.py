from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from doctor.models import *
from django.db.models import Q

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


def doctor_dashboard(request):
    return