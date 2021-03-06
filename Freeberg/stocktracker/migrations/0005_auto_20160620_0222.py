# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-19 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocktracker', '0004_auto_20160613_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='dividend',
            field=models.FloatField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='stock',
            name='ebitda',
            field=models.FloatField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='stock',
            name='get_high',
            field=models.FloatField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='stock',
            name='get_low',
            field=models.FloatField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='stock',
            name='market_cap',
            field=models.FloatField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='stock',
            name='pb_ratio',
            field=models.FloatField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='stock',
            name='price_change',
            field=models.FloatField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='stock',
            name='close',
            field=models.FloatField(default=1),
        ),
        migrations.AlterField(
            model_name='stock',
            name='open',
            field=models.FloatField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='stock',
            name='volume',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
