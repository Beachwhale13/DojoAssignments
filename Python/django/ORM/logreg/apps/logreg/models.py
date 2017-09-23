# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import datetime
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
DATE_STR_REGEX = re.compile(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) == 0:
            errors['first_name'] = "Please enter a first name"
        elif len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be more than 2 characters"
        elif any([letter.isdigit() for letter in postData['first_name']]):
            errors['first_name'] = "First name must only contains letters"

        if len(postData['last_name']) == 0:
            errors['last_name'] = "Please enter a last name"
        elif len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be more than 2 characters"
        elif any([letter.isdigit() for letter in postData['last_name']]):
            errors['last_name'] = "Last name must only contains letters"

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


class LoginManager(models.Manager):
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
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    objects=UserManager()
    objects=LoginManager()
