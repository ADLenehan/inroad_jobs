# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-07 00:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_signup_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='purpose',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='landing.Purpose'),
        ),
    ]
