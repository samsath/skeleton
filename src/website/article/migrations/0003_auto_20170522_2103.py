# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-22 21:03
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import mediastore.fields.related


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20170410_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='main_image',
            field=mediastore.fields.related.MediaField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_main_image', to='mediastore.Media'),
        ),
    ]
