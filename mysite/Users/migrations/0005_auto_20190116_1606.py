# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-16 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_auto_20190116_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='request_serial_num',
            field=models.IntegerField(unique=True, verbose_name='request_serial_num'),
        ),
    ]