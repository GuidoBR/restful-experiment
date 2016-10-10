# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restful', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.EmailField(default='default_user', max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateField(auto_now_add=True),
        ),
    ]