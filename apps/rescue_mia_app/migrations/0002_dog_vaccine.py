# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-11 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rescue_mia_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='vaccine',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]