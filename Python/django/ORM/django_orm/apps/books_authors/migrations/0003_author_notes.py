# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors', '0002_auto_20170922_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]