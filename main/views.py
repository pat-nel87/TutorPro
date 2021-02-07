from django.shortcuts import render, HttpResponse, redirect
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
        #  Rene changed httpresponst to redirect
        # in the forms.py, do i need to add in the subject model to be created
           return redirect('/index/tutor_pro')
           
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
           return redirect('/index/stu_pro')
    
    context = {
        'user': user,
        'form': form
        }
    return render(request, 'stureg.html', context)

# Rene code starts here
def tutor_pro(request):
    user = request.user
    this_user = Tutor_Profile.objects.filter(email=user)
    all_students = Student_Profile.objects.all()
    context = {
        'all_students': all_students,
        'this_tutor': this_user[0],
    }
    return render(request, 'tutor_pro.html', context)

def stu_pro(request):
    all_tutors = Tutor_Profile.objects.all()
    context = {
        'all_tutors': all_tutors,
    }
    return render(request,'stu_pro.html', context)

def profile_student(request, stu_id):
    this_student = Student_Profile.objects.get(id=stu_id)
    context = {
        'this_student': this_student,
    }
    return render(request,'profile_student.html', context)