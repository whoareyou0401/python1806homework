# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-27 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='学生名字')),
                ('age', models.IntegerField(default=18, verbose_name='年纪')),
                ('score', models.IntegerField(verbose_name='成绩')),
            ],
        ),
    ]
