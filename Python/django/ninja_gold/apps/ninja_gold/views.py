# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *
import random
from time import gmtime, strftime

# Create your views here.
def index(request):
    if not "gold" in request.session:
        request.session['gold'] = 0
    if not "activities" in request.session:
        request.session['activities'] = []
    if not "happenings" in request.session:
        request.session['happenings'] = {}
    return render(request, 'ninja_gold/index.html', )

def process(request):
    if request.method == "POST":
        if request.POST['building'] == "farm":
            winnings = (random.randrange(10,21))
        if request.POST['building'] == "cave":
            winnings = (random.randrange(5,11))
        if request.POST['building'] == "house":
            winnings = (random.randrange(2,6))
        if request.POST['building'] == "casino":
            winnings = (random.randrange(-50,61))

        if winnings > 0:
            color = "green"
        else:
            color = "red"

        request.session['happenings'] = {
            'building': request.POST['building'],
            'winnings': winnings,
            'color': color,
            "datetime": strftime("%Y/%m/%d %-I:%M %p", gmtime()),
            }

        request.session['activities'].append(request.session['happenings'])
        request.session['gold'] += winnings

        return redirect('/')
    else:
        return redirect('/')

def reset(request):
    del request.session['gold']
    del request.session['activities']
    return redirect('/')
