from django.shortcuts import render
from .models import Department,Doctors
from .forms import BookingForm

# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def booking(request):
    if request.method =='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form=BookingForm
    dict_form={
        'form':form
    }
    return render(request,"booking.html",dict_form)

def doctor(request):
    dict_doc={
        'doc':Doctors.objects.all()
    }
    return render(request,"doctor.html",dict_doc)
    

def contact(request):
    return render(request,"contact.html")
def department(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request,"department.html",dict_dept)

