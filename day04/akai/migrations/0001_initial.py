# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-22 01:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='语言名字')),
                ('desc', models.CharField(max_length=200, null=True, verbose_name='描述')),
            ],
        ),
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='工程师')),
                ('sex', models.CharField(default='男', max_length=4)),
                ('start', models.DateTimeField(auto_now_add=True, verbose_name='从业时间')),
                ('comlanguage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akai.ComLanguage', verbose_name='编程语言')),
            ],
        ),
    ]