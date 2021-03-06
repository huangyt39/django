# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-17 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180917_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='blog.Category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]
