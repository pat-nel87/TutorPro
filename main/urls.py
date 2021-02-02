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
    path('/stureg', views.student_reg, name='stureg')
       
    ]