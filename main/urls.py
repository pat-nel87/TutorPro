# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 21:30:41 2021

@author: Patrick
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/tutreg', views.tutor_reg, name='tutor_reg'),
    path('/stureg', views.student_reg, name='stureg'),
    path('/tutor_pro', views.tutor_pro, name='tutor_pro'),
    path('/stu_pro', views.stu_pro, name='stu_pro'), 
    path('/profile_student/<int:stu_id>', views.profile_student, name='profile_student'),
    path('/profile_tutor/<int:tutor_id>', views.profile_tutor, name='profile_tutor'),
    ]