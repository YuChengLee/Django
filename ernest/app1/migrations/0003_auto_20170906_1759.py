# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-06 17:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20170906_1712'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chice',
            new_name='Choice',
        ),
    ]