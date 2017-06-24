# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-18 21:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('enquiry', '0002_newslettersignup'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newslettersignup',
            old_name='first_name',
            new_name='_name',
        ),
        migrations.RemoveField(
            model_name='enquiry',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='enquiry',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='newslettersignup',
            name='last_name',
        ),
        migrations.AddField(
            model_name='enquiry',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='Name'),
            preserve_default=False,
        ),
    ]