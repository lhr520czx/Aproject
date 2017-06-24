# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-23 06:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddScheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_name', models.CharField(default='', max_length=10, verbose_name='类型')),
                ('content', models.CharField(default='', max_length=50, verbose_name='具体内容')),
                ('time', models.CharField(default='', max_length=20, verbose_name='要求完成时间')),
                ('principal', models.CharField(default='', max_length=10, verbose_name='负责人')),
                ('complete_status', models.TextField(default='', verbose_name='完成情况')),
                ('schedule', models.CharField(default='', max_length=10, verbose_name='进度')),
                ('is_finished', models.BooleanField(default=False, verbose_name='是否完成')),
            ],
        ),
        migrations.CreateModel(
            name='Scheme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', max_length=20, verbose_name='方案类别')),
                ('principal', models.CharField(default='', max_length=20, verbose_name='负责人')),
                ('member', models.CharField(default='', max_length=30, verbose_name='成员')),
                ('budget', models.FloatField(default=0, verbose_name='预算')),
                ('actual_cost', models.FloatField(default=0, verbose_name='实际费用')),
                ('start_time', models.CharField(default='', max_length=20, verbose_name='方案开始时间')),
                ('end_time', models.CharField(default='', max_length=20, verbose_name='方案结束时间')),
                ('content', models.TextField(default='', verbose_name='内容')),
                ('remark', models.CharField(default='', max_length=100, verbose_name='备注')),
                ('file', models.FileField(blank=True, default='', null=True, upload_to='xc/files/%Y/%m', verbose_name='附件')),
            ],
            options={
                'verbose_name': '宣传方案申请',
                'verbose_name_plural': '宣传方案申请',
            },
        ),
    ]
