# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:57:30 2021

@author: Patrick
"""

from django.urls import path

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('/register', views.register, name="register"),
    path('/log_on', views.log_on, name="log_on"),
    path('/log_out', views.log_out, name="log_out")
    
    ]