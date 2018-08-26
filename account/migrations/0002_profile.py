# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-22 07:33
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '1234567890'. Up to 10 digits allowed.", regex='^\\+?1?\\d{9,10}$')], verbose_name='Phone Number')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.college_list_yuva')),
            ],
        ),
    ]