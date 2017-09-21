# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

from models import *

# Create your views here.

def index(request):
    request.session['counter'] = 0
    return render(request, 'random_word/index.html')

def random_word(request):
    request.session['counter'] += 1
    request.session['word'] = get_random_string(length=14)
    return render(request, 'random_word/index.html')

def generate(request):
    if request.method == "POST":
        return redirect('/random_word')

def reset(request):
    del request.session['counter']
    del request.session['word']
    return redirect('/')
