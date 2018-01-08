# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0015_auto_20170829_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment_user',
            name='Company',
        ),
        migrations.RemoveField(
            model_name='comment_user',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='position',
        ),
        migrations.AddField(
            model_name='comment',
            name='Company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jobs.Company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user_position',
            field=models.CharField(default='testpos', max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Comment_User',
        ),
    ]
