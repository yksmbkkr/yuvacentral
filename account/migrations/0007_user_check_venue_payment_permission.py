# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-15 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20181005_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_check',
            name='venue_payment_permission',
            field=models.BooleanField(default=False),
        ),
    ]