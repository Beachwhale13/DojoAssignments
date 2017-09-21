# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django import forms

from models import *
# Create your views here.

def index(request):
    if not "word_array" in request.session:
        request.session['word_array'] = []
    return render(request, 'session_words/index.html')

def process(request):
    if request.method == "POST":
        request.session['word'] = request.POST['word']
        request.session['color'] = request.POST['color']
        if 'font' in request.POST:
            request.session['font'] = request.POST['font']
        else:
            if not 'font' in request.session:
                request.session['font'] = "false"
            else:
                request.session['font'] = "false"
        request.session['word_array'].append(request.POST)
        return redirect('/')

def clear(request):
    del request.session['word_array']
    return redirect('/')
