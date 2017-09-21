# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from models import *
# Create your views here.

def index(request):
    request.session['counter'] = 0
    return render(request, 'survey_form/index.html')

def reload(request):
    return render(request,'survey_form/index.html')

def process(request):
    if request.method == "POST":
        request.session['counter'] += 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    return render(request, 'survey_form/result.html')
