# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 13:46:38 2021

@author: Patrick
"""

from django import forms
from .models import Tutor_Profile, Student_Profile

class Tutor_Form(forms.ModelForm):
    # Rene question to reasearch later, 
    # what does the Meta class do in this py?
    class Meta:
        model = Tutor_Profile
        exclude = ['user','created_at','uploaded_at']

class Student_Form(forms.ModelForm):
    
    class Meta:
        model = Student_Profile
        exclude = ['user','created_at','uploaded_at']


