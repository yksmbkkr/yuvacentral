# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-15 13:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vimarsh18', '0013_auto_20181015_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rid', models.CharField(max_length=20)),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vimarsh18.session_vim')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]