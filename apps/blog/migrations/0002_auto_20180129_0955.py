# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-29 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='front_image',
            field=models.ImageField(blank=True, help_text='图片尺寸：295 x 230', null=True, upload_to='blog/images/', verbose_name='封面图'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='top_image',
            field=models.ImageField(blank=True, help_text='图片尺寸：750 x 415', null=True, upload_to='blog/images/', verbose_name='顶部图'),
        ),
    ]
