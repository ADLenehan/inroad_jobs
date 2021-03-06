# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-02 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_remove_position_postal_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='city',
            field=models.CharField(max_length=125, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='indeed_id',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='job_title',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='state',
            field=models.CharField(max_length=125, null=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='url',
            field=models.CharField(max_length=125, null=True),
        ),
    ]
