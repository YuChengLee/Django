# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 18:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20170906_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('brithday', models.DateTimeField()),
            ],
        ),
        migrations.AlterModelManagers(
            name='question',
            managers=[
                ('q', django.db.models.manager.Manager()),
            ],
        ),
    ]
