# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-03 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_host_shelltask'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelltask',
            name='callsign',
            field=models.CharField(default='test', max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
