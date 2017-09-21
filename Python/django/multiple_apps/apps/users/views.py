# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *

# Create your views here.
def display(request):
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)

def register(request):
    response = "placeholder for users to create new user record"
    return HttpResponse(response)

def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)
