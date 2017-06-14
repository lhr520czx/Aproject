# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 13:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('xuanchuan', '0001_initial'),
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propagateplan',
            name='accept_user',
            field=models.ManyToManyField(related_name='plan_accept_user', to=settings.AUTH_USER_MODEL, verbose_name='接受人'),
        ),
        migrations.AddField(
            model_name='propagateplan',
            name='main',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xuanchuan.DraftBase', verbose_name='基础信息'),
        ),
        migrations.AddField(
            model_name='propagateplan',
            name='office',
            field=models.ManyToManyField(to='users.Office', verbose_name='类型'),
        ),
        migrations.AddField(
            model_name='propagateplan',
            name='opinion',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='xuanchuan.Opinion', verbose_name='领导意见'),
        ),
    ]
