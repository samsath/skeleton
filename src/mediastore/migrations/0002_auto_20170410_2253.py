# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 22:53
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediastore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='end_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Middle or End Name'),
        ),
        migrations.AddField(
            model_name='map',
            name='start_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Start Name'),
        ),
        migrations.AlterField(
            model_name='map',
            name='end',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Middle or End'),
        ),
    ]
