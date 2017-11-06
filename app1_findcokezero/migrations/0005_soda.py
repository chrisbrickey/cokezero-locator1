# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1_findcokezero', '0004_auto_20171002_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Soda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('abbreviation', models.CharField(max_length=2)),
                ('low_calorie', models.BooleanField(default=True)),
            ],
        ),
    ]