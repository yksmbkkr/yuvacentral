# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-15 07:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vimarsh18', '0011_auto_20181013_2152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='id_card',
            options={'ordering': ['reg_no']},
        ),
    ]