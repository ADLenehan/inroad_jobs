# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-29 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='position',
            name='experience',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Experience'),
        ),
    ]
