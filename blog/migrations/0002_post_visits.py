# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 02:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visits',
            field=models.IntegerField(default=0),
        ),
    ]
