# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-27 21:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20170602_0343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='indeed',
        ),
        migrations.AddField(
            model_name='position',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 6, 27, 21, 16, 17, 815422, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='position',
            name='city',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='indeed_id',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='job_title',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='state',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='url',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
    ]