# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request, "logreg/index.html")

def register(request):
    if "route" in request.session:
        del request.session['route']
    if "user_id" in request.session:
        del request.session['user_id']

    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request,error, extra_tags=tag)

        else:
            hashpass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(first_name=request.POST['first_name'], last_name = request.POST['last_name'], email=request.POST['email'], password = hashpass)

            user = User.objects.last()
            if not 'user_id' in request.session:
                request.session['user_id'] = user.id

            if not 'request' in request.session:
                request.session['route'] = request.POST['route']

            context = {'user':user}
            return render(request, "logreg/success.html", context)
    return redirect('/')

def login(request):
    if "route" in request.session:
        del request.session['route']
    if "user_id" in request.session:
        del request.session['user_id']

    if request.method == "POST":
        errors = User.objects.basic_login_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request,error, extra_tags=tag)
                return redirect('/')
        else:
            user = User.objects.get(email = request.POST['email'])
            if not 'user_id' in request.session:
                request.session['user_id'] = user.id

            if not 'request' in request.session:
                request.session['route'] = request.POST['route']

                context = {'user':user}
                return render(request, "logreg/success.html", context)
    return render(request, "logreg/success.html")
