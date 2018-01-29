# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-29 10:20
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='课程类别')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='课程名字')),
                ('desc', models.CharField(max_length=300, verbose_name='课程描述')),
                ('detail', DjangoUeditor.models.UEditorField(default='', verbose_name='课程详情')),
                ('degree', models.CharField(choices=[('cj', '初级'), ('zj', '中级'), ('gj', '高级')], max_length=2, verbose_name='难度')),
                ('learn_times', models.IntegerField(default=0, verbose_name='学习长度（分钟数）')),
                ('students', models.IntegerField(default=0, verbose_name='学习人数')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('image', models.ImageField(upload_to='courses/%y/%m', verbose_name='封面图')),
                ('click_nums', models.IntegerField(default=0, verbose_name='点击人数')),
                ('youneed_know', models.CharField(default='', max_length=300, verbose_name='课程须知')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Category', verbose_name='课程类别')),
            ],
            options={
                'verbose_name': '课程',
                'verbose_name_plural': '课程',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='课程标签')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='courses.Tag', verbose_name='课程标签'),
        ),
    ]
