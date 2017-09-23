# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from models import *

# Create your views here.
def index(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'semi_restful/index.html', context)

def adduser(request):
    return render(request, 'semi_restful/adduser.html')

def process(request):
    if request.method == "POST":

        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])

    return redirect('/')

def show(request, number):
    user=User.objects.get(id=number)
    context={'user': user}
    return render(request, "semi_restful/user.html", context)

def edit(request, number):
    context = {"number": number}
    return render(request, "semi_restful/edit.html", context)

def update(request):
    if request.method == "POST":
        User.objects.filter(id=request.POST['user_id']).update(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email=request.POST['email'])
    return redirect('/')

def delete(request, number):
    user = User.objects.get(id=number)
    user.delete()
    return redirect('/')
