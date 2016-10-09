# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=254)),
                ('phones', models.CharField(max_length=254)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('last_login', models.CharField(max_length=254)),
                ('token', models.CharField(max_length=254)),
            ],
        ),
    ]