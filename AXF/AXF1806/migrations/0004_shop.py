# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-03 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AXF1806', '0003_mustbuy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=255, verbose_name='图片链接')),
                ('name', models.CharField(max_length=100, verbose_name='介绍名字')),
                ('trackid', models.CharField(max_length=100, verbose_name='trackid')),
            ],
            options={
                'db_table': 'axf_shop',
            },
        ),
    ]