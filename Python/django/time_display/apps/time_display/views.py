# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

from models import *

# Create your views here.

def index(request):
    context = {
    "date": strftime("%b %d, %Y", gmtime()),
    "time": strftime("%I:%M %p", gmtime()),
    }

    return render(request, 'time_display/index.html', context)
