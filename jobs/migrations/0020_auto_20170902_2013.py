# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0019_auto_20170902_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='position',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jobs.Position'),
        ),
        migrations.AddField(
            model_name='position',
            name='board',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='jobs.Board'),
            preserve_default=False,
        ),
    ]
