# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-03 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.GenericIPAddressField()),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Hosts',
            },
        ),
        migrations.CreateModel(
            name='ShellTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=1000)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Host')),
            ],
            options={
                'db_table': 'Shell Tasks',
            },
        ),
    ]
