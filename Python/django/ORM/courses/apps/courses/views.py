# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from models import *

# Create your views here.
def index(request):
    courses = Course.objects.all
    context = {'courses': courses}
    return render(request, "courses/index.html", context)

def add(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request,error, extra_tags=tag)
        else:
            Course.objects.create(name=request.POST['name'], desc = request.POST['desc'] )
            # Description.objects.create(course=Course.objects.last(),desc = request.POST['desc'])

    return redirect('/')

def delete(request, number):
    selection = Course.objects.get(id=number)
    context={'selection': selection}
    return render(request, 'courses/confirm.html', context)

def destroy(request, number):
    d = Course.objects.get(id=number)
    d.delete()
    return redirect('/')
