# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-22 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20170922_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='img',
            field=models.ImageField(upload_to='photoimg'),
        ),
    ]