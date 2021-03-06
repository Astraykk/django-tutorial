# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-16 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_auto_20190115_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='authority',
            field=models.IntegerField(default=5, verbose_name='authority'),
        ),
        migrations.AlterField(
            model_name='task',
            name='request_serial_num',
            field=models.IntegerField(verbose_name='request_serial_num'),
        ),
        migrations.AlterField(
            model_name='users',
            name='authority',
            field=models.CharField(default='common_user', max_length=20, verbose_name='authority'),
        ),
    ]
