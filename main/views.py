from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Tutor_Profile, Student_Profile
from .forms import Tutor_Form, Student_Form



def index(request):
    user = request.user
    return render(request, "index.html")

def tutor_reg(request):
    user = request.user
    form = Tutor_Form
    if request.method == 'POST':           
           user = request.user
           first_name = request.POST['first_name']
           last_name = request.POST['last_name']
           email = request.POST['email']
           street_addr = request.POST['street_addr']
           city = request.POST['city']
           state = request.POST['state']
           country = request.POST['country']
           desc = request.POST['desc']
           new_tutor = Tutor_Profile.objects.create(first_name=first_name, last_name=last_name, email= email, street_addr = street_addr, city = city, state= state, country = country, desc = desc, user=user)
           new_tutor.save()
           return HttpResponse(f"{new_tutor}")
           
    else:
        context = {
            'user': user,
            'form': form
            }
        return render(request, 'tutreg.html', context)
    

def student_reg(request):
    user = request.user
    form = Student_Form
    if request.method == 'POST':           
           user = request.user
           first_name = request.POST['first_name']
           last_name = request.POST['last_name']
           email = request.POST['email']
           street_addr = request.POST['street_addr']
           city = request.POST['city']
           state = request.POST['state']
           country = request.POST['country']
           desc = request.POST['desc']
           new_student = Student_Profile.objects.create(first_name=first_name, last_name=last_name, email= email, street_addr = street_addr, city = city, state= state, country = country, desc = desc, user=user)
           new_student.save()
           return HttpResponse(f"{new_student}")
    
    context = {
        'user': user,
        'form': form
        }
    return render(request, 'stureg.html', context)