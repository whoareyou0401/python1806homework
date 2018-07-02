# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-28 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AXF', '0008_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_name', models.CharField(max_length=16, unique=True)),
                ('u_password', models.CharField(max_length=128)),
                ('u_email', models.CharField(max_length=64, unique=True)),
                ('u_icon', models.ImageField(upload_to='icons')),
                ('is_delete', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'axf_user',
            },
        ),
    ]
