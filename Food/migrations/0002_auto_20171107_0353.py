# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 03:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='food_name',
            new_name='movie_name',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='food_price',
            new_name='ticket_price',
        ),
        migrations.AddField(
            model_name='food',
            name='gener',
            field=models.CharField(default='abc', max_length=10),
        ),
    ]
