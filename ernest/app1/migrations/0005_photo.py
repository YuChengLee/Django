# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-22 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20170920_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photo_home')),
            ],
        ),
    ]