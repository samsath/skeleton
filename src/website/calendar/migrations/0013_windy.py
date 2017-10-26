# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-25 00:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendar', '0012_auto_20170628_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Windy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='Time')),
                ('timestamp', models.IntegerField(blank=True, null=True, verbose_name='Timestamp')),
                ('gust', models.FloatField(blank=True, null=True, verbose_name='GUST')),
                ('ugrd', models.FloatField(blank=True, null=True, verbose_name='UGRD')),
                ('vgrd', models.FloatField(blank=True, null=True, verbose_name='VGRD')),
                ('tmp', models.FloatField(blank=True, null=True, verbose_name='Temperature')),
                ('prate', models.CharField(blank=True, max_length=255, null=True, verbose_name='PRATE')),
                ('cwat', models.FloatField(blank=True, null=True, verbose_name='CWAT')),
                ('tcdc_low', models.FloatField(blank=True, null=True, verbose_name='TCDC_LOW')),
                ('tcdc_mid', models.FloatField(blank=True, null=True, verbose_name='TCDC_MID')),
                ('tcdc_high', models.FloatField(blank=True, null=True, verbose_name='TCDC_HIGH')),
                ('rh', models.FloatField(blank=True, null=True, verbose_name='RH')),
                ('pres_old', models.FloatField(blank=True, null=True, verbose_name='PRES_OLD')),
                ('pres', models.FloatField(blank=True, null=True, verbose_name='PRES')),
                ('dpt', models.FloatField(blank=True, null=True, verbose_name='DPT')),
                ('cloud_base', models.FloatField(blank=True, null=True, verbose_name='CLOUD_BASE')),
                ('swellDirection', models.FloatField(blank=True, null=True, verbose_name='swellDirection')),
                ('swellSize', models.FloatField(blank=True, null=True, verbose_name='swellSize')),
                ('swellPeriod', models.FloatField(blank=True, null=True, verbose_name='swellPeriod')),
                ('water_temp', models.FloatField(blank=True, null=True, verbose_name='water_temp')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendar.Calendar')),
            ],
            options={
                'verbose_name_plural': 'Windy',
                'verbose_name': 'Windy',
                'ordering': ['day', 'time'],
            },
        ),
    ]