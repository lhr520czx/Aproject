# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0002_auto_20170620_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worktarget',
            name='target_user',
            field=models.CharField(default='', max_length=10, verbose_name='负责人'),
        ),
    ]
