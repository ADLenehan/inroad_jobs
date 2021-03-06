# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-02 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20170602_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='company',
        ),
        migrations.AddField(
            model_name='position',
            name='city',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='indeed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='position',
            name='indeed_id',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='postal_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='state',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
        migrations.DeleteModel(
            name='Office',
        ),
    ]
