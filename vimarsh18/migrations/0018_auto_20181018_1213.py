# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-18 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vimarsh18', '0017_id_special'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session_vim',
            name='info',
            field=models.CharField(max_length=350),
        ),
        migrations.AlterField(
            model_name='session_vim',
            name='topic',
            field=models.CharField(max_length=250),
        ),
    ]
