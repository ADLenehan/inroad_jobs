# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0018_auto_20170902_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='picture_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jobs.Company'),
        ),
    ]