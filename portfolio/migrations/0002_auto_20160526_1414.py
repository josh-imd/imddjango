# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-26 21:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagegallery',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imd.Service'),
        ),
    ]