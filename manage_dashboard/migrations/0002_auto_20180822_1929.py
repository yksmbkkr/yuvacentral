# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-22 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='up_events',
            name='date',
            field=models.CharField(max_length=50),
        ),
    ]
