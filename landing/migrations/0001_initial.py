# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]