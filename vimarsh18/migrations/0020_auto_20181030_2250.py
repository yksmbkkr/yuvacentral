# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-30 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vimarsh18', '0019_auto_20181023_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='overall_experience',
            new_name='admin_satisfaction',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='participation_experience',
            new_name='content_use',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='session_content',
            new_name='overall_satisfaction',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='reg_no',
            field=models.CharField(max_length=20, verbose_name='Registration Number'),
        ),
    ]
