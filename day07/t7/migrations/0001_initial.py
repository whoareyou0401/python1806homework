# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-27 04:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='班级名字')),
                ('type', models.CharField(max_length=20, verbose_name='班级类型')),
            ],
        ),
        migrations.CreateModel(
            name='Stu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名字')),
                ('age', models.IntegerField(default=18, verbose_name='年纪')),
                ('score', models.IntegerField(verbose_name='成绩')),
                ('grade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='t7.Grade', verbose_name='所属班级')),
            ],
        ),
    ]
