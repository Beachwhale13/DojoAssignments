# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
import bcrypt
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request, "belt_review/index.html")

def register(request):
    if "user_id" in request.session:
        del request.session['user_id']

    if request.method == "POST":
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request,error, extra_tags=tag)

        else:
            hashpass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            User.objects.create(name=request.POST['name'], alias = request.POST['alias'], email=request.POST['email'], password = hashpass)

            user = User.objects.last()
            if not 'user_id' in request.session:
                request.session['user_id'] = user.id
            return redirect('/books')

    return redirect('/')

def books(request):
    user = User.objects.get(id=request.session['user_id'])
    reviews = Review.objects.order_by('-created_at')[:3]
    books = Book.objects.annotate(num_review=Count('bookreviews'))
    context = {'user':user, 'reviews':reviews, 'books': books}
    return render(request, "belt_review/home.html", context)

def login(request):
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
                return redirect('/books')
    return redirect('/')

def add(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, "belt_review/add.html", context)

def process_add(request):
    if request.method == "POST":
        errors = {}
        if len(request.POST['title']) == 0:
            errors['title'] = "Please enter a title"
        if len(request.POST['review']) == 0:
            errors['review'] = "Please enter a review"
        if request.POST['select_author'] == "None" and len(request.POST['author']) == 0:
            errors['author'] = "Please enter an author"
        if len(request.POST['select_author']) and request.POST['select_author'] != "None" and len(request.POST['author']):
            errors['author'] = "Please enter only one author"
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request,error, extra_tags=tag)
                return redirect('/add')


        if request.POST['select_author'] != "None": #author was selected
            try:
                book = Book.objects.get(name=request.POST['title']) #book already exists --> add the review
                Review.objects.create(comment=request.POST['review'], rating=request.POST['rating'], book=Book.objects.get(name=request.POST['title']), user=User.objects.get(id=request.session['user_id']))
                bookrev = Book.objects.get(name=request.POST['title'])
                return redirect(reverse('showbook', kwargs={'number':bookrev.id}))
            except Book.DoesNotExist: #book doesn't exist --> add book and add review
                Book.objects.create(name=request.POST['title'], author=Author.objects.get(name=request.POST['select_author']))
                Review.objects.create(comment=request.POST['review'], rating=request.POST['rating'], book=Book.objects.last(), user=User.objects.get(id=request.session['user_id']))
                bookrev = Book.objects.get(name=request.POST['title'])
                return redirect(reverse('showbook', kwargs={'number':bookrev.id}))

        else: #author was typed in
            try:
                author = Author.objects.get(name=request.POST['author']) #typed in author exists
                try:
                    book = Book.objects.get(name=request.POST['title']) #book already exists --> add the review
                    Review.objects.create(comment=request.POST['review'], rating=request.POST['rating'], book=Book.Objects.get(name=request.POST['title']), user=User.objects.get(id=request.session['user_id']))
                    bookrev = Book.objects.get(name=request.POST['title'])
                    return redirect(reverse('showbook', kwargs={'number':bookrev.id}))
                except Book.DoesNotExist: #author exists, but book doesn't exist --> create book and review
                    Book.objects.create(name=request.POST['title'], author=Author.objects.get(name=request.POST['author']))
                    Review.objects.create(comment=request.POST['review'], rating=request.POST['rating'], book=Book.objects.last(), user=User.objects.get(id=request.session['user_id']))
                    bookrev = Book.objects.get(name=request.POST['title'])
                    return redirect(reverse('showbook', kwargs={'number':bookrev.id}))
            except Author.DoesNotExist: #typed in author doesn't exist --> create author, book, and review
                if len(request.POST['author']) != 0:
                    Author.objects.create(name=request.POST['author'])
                    Book.objects.create(name=request.POST['title'], author=Author.objects.last())
                    Review.objects.create(comment=request.POST['review'], rating=request.POST['rating'], book=Book.objects.last(), user=User.objects.get(id=request.session['user_id']))
                    bookrev = Book.objects.get(name=request.POST['title'])
                    return redirect(reverse('showbook', kwargs={'number':bookrev.id}))
    return redirect('/books')


def addreview(request):
    if request.method == "POST":
        place=request.POST['book']
        Review.objects.create(comment=request.POST['review'], rating=request.POST['rating'], book=Book.objects.get(id=request.POST['book']), user=User.objects.get(id=request.session['user_id']))
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)

def bookshow(request, number):
    book = Book.objects.get(id=number)
    reviews = Review.objects.all()
    context = {'book': book, 'reviews': reviews}
    return render(request, "belt_review/book.html", context)

def show(request, number):
    user = User.objects.get(id=number)
    reviews = Review.objects.filter(user__id=number)
    count = len(reviews)
    context = {'user': user, 'reviews': reviews, 'count': count}
    return render(request, "belt_review/userreview.html", context)

def delete(request, number):
    d = Review.objects.get(id=number)
    d.delete()
    return redirect('/books')

def logout(request):
    del request.session['user_id']
    return redirect('/')
