# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-24 10:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sysconf', '0004_auto_20180124_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='sortNume',
            new_name='sortNumber',
        ),
    ]
