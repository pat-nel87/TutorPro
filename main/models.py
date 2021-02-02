from django.db import models
from django.contrib.auth.models import User

class Tutor_Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)   
    email = models.EmailField(unique=True)     
    street_addr = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    desc = models.TextField()       
    user = models.ForeignKey(User,related_name="profile_Tutor", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Student_Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)   
    email = models.EmailField(unique=True)     
    street_addr = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    desc = models.TextField()       
    user = models.ForeignKey(User,related_name="profile_Student", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Subject(models.Model):
    name = models.CharField(max_length=255)
    tutored_by = models.ManyToManyField(Tutor_Profile, related_name="subject")
    requested_by = models.ManyToManyField(Student_Profile, related_name="subject_request")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
class Post(models.Model):
    text = models.TextField()
    posted_by = models.ForeignKey(User, related_name="userpost", on_delete=models.CASCADE)
    subject_listed = models.ManyToManyField(Subject, related_name="subject_request")
    


    
    
