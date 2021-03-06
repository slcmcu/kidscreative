# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-24 13:19
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标签名称')),
                ('colorNum', models.IntegerField(default=0, help_text='1-10代表标签不同颜色，0为默认', verbose_name='显示颜色')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='标题')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('modify_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('click_num', models.IntegerField(default=0, verbose_name='访问次数')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('front_image', models.ImageField(blank=True, null=True, upload_to='blog/images/', verbose_name='封面图')),
                ('top_image', models.ImageField(blank=True, null=True, upload_to='blog/images/', verbose_name='顶部图')),
                ('label', models.ManyToManyField(related_name='tag', to='blog.ArticleLabel', verbose_name='标签')),
            ],
            options={
                'verbose_name': '文章管理',
                'verbose_name_plural': '文章管理',
            },
        ),
    ]
