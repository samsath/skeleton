# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubsessions', '0002_session_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='club',
            field=models.BooleanField(default=False, verbose_name='At Club'),
        ),
        migrations.AddField(
            model_name='session',
            name='list_description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='List Description'),
        ),
        migrations.AlterField(
            model_name='session',
            name='day_of_week',
            field=models.CharField(choices=[('0', 'Monday'), ('1', 'Tuesday'), ('2', 'Wednesday'), ('3', 'Thursday'), ('4', 'Friday'), ('5', 'Saturday'), ('6', 'Sunday')], max_length=10, verbose_name='Day of Week'),
        ),
    ]
