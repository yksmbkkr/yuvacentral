# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-15 18:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vimarsh18', '0015_venue_payment_stats'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venue_payment_stats',
            options={'ordering': ['-created_at']},
        ),
    ]