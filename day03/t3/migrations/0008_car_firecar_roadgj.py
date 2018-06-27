# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-21 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('t3', '0007_cat_dog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roadgj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speed', models.IntegerField(default=10)),
                ('humens', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('roadgj_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='t3.Roadgj')),
                ('brand', models.CharField(max_length=20)),
            ],
            bases=('t3.roadgj',),
        ),
        migrations.CreateModel(
            name='FireCar',
            fields=[
                ('roadgj_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='t3.Roadgj')),
                ('time', models.TimeField(auto_now_add=True)),
            ],
            bases=('t3.roadgj',),
        ),
    ]
