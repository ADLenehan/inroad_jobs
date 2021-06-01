# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0013_comment_board'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.AddField(
            model_name='board',
            name='wish',
            field=models.BooleanField(default=False),
        ),
    ]