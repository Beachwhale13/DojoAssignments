# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import *

# Create your views here.

def index(request):
    if not "account" in request.session:
        request.session['account'] = 0
    if not "cart" in request.session:
        request.session['cart'] = 0
    if not "items" in request.session:
        request.session['items'] = 0
    return render(request, "amadon/index.html")

def buy(request):
    if request.method == "POST":
        request.session['items'] += int(request.POST['quantity'])
        request.session['cart'] += int(request.POST['quantity'])*float(request.POST['price'])
    return redirect('/checkout')

def checkout(request):
    request.session['account'] += request.session['cart']
    return render(request, "amadon/checkout.html")

def back(request):
    del request.session['cart']
    return redirect('/')
