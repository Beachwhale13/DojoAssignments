# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import datetime
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) == 0:
            errors['name'] = "Please enter a name"
        elif len(postData['name']) < 8:
            errors['name'] = "Name should be more than 8 characters"
        elif any([letter.isdigit() for letter in postData['name']]):
            errors['name'] = "Name must only contains letters"

        if len(postData['alias']) == 0:
            errors['alias'] = "Please enter an alias"
        elif len(postData['alias']) < 2:
            errors['alias'] = "Alias should be more than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "Enter a valid email"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please enter a valid email in email format"
        else:
            try:
                User.objects.get(email=postData['email'])
                errors['email'] = "Email is already registered, please enter another"
            except ObjectDoesNotExist:
                pass

        if len(postData['password']) == 0:
            errors['password'] = "Please enter a password"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be longer than 8 characters"
        if postData['password'] != postData['cpass']:
            errors['password'] = "Confirmation password does not match the password"
        return errors;

    def basic_login_validator(self, postData):
        errors = {}
        if len(postData['email']) == 0:
            errors['email'] = "Please enter an email"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please enter a valid email in email format"
        else:
            try:
                user = User.objects.get(email=postData['email'])
                if bcrypt.checkpw(postData['password'].encode(), user.password.encode()) != True:
                    errors['password'] = "Email and password doesn't match"
            except ObjectDoesNotExist:
                errors['password'] = "Email is not registered, please register first"
        if len(postData['password']) == 0:
            errors['password'] = "Please enter a password"
        return errors;

class User(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects=UserManager()

class Author(models.Model):
    name = models.CharField(max_length=255)

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name = "books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Review(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    book = models.ForeignKey(Book, related_name = "bookreviews")
    user = models.ForeignKey(User, related_name ="userreviews")
