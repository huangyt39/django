# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-17 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('discription', models.TextField()),
                ('body', models.TextField()),
                ('timestamp', models.DateField()),
            ],
        ),
    ]
