# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-11 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vimarsh18', '0009_session_vim'),
    ]

    operations = [
        migrations.CreateModel(
            name='id_card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=50)),
                ('id_img', models.ImageField(null=True, upload_to='id_cards')),
            ],
        ),
    ]
