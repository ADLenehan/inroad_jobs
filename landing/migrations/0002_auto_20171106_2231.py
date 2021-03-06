# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(error_messages={'required': 'Please provide your email address.', 'unique': 'An account with this email exist.'}, max_length=254, unique=True),
        ),
    ]
