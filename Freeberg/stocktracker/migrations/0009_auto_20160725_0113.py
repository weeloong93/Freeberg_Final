# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-24 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocktracker', '0008_auto_20160725_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='a_gain',
            field=models.CharField(default='-', max_length=10000000),
        ),
        migrations.AddField(
            model_name='stock',
            name='peg',
            field=models.CharField(default='-', max_length=1000),
        ),
        migrations.AddField(
            model_name='stock',
            name='revenue',
            field=models.CharField(default='-', max_length=100000),
        ),
    ]
