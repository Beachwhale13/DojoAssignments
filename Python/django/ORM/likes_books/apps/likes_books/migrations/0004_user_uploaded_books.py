# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes_books', '0003_auto_20170922_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='uploaded_books',
            field=models.ManyToManyField(related_name='uploader', to='likes_books.Book'),
        ),
    ]
