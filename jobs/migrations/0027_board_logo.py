# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-07 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0026_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='images/publishers'),
        ),
    ]
