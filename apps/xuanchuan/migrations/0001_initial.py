# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 15:36
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='类别名称')),
                ('status', models.CharField(choices=[('stop', '停用'), ('active', '启用')], default='active', max_length=6, verbose_name='状态')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='申请时间')),
                ('create_user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '类别',
                'verbose_name_plural': '类别',
            },
        ),
        migrations.CreateModel(
            name='CategoryCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tv_count', models.IntegerField(default=0, verbose_name='电视媒体类')),
                ('internet_count', models.IntegerField(default=0, verbose_name='网络媒体类')),
                ('lift_count', models.IntegerField(default=0, verbose_name='电梯海报类')),
                ('news_count', models.IntegerField(default=0, verbose_name='新闻媒体类')),
                ('webo_count', models.IntegerField(default=0, verbose_name='微博微信类')),
                ('other_count', models.IntegerField(default=0, verbose_name='其他')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '宣传信息发布统计',
                'verbose_name_plural': '宣传信息发布统计',
            },
        ),
        migrations.CreateModel(
            name='DraftBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('status', models.CharField(choices=[('wait', '待审批'), ('success', '已审批')], default='wait', max_length=10, verbose_name='状态')),
                ('style', models.CharField(default='', max_length=20, verbose_name='表单申请类型')),
                ('add_time', models.DateTimeField(default='', verbose_name='申请时间')),
                ('accept_user', models.ManyToManyField(related_name='accept_user', to=settings.AUTH_USER_MODEL, verbose_name='接受人')),
                ('draft_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='draft_user', to=settings.AUTH_USER_MODEL, verbose_name='起草人')),
            ],
            options={
                'verbose_name': '基础表',
                'verbose_name_plural': '基础表',
            },
        ),
        migrations.CreateModel(
            name='ItemMake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='宣传品名称')),
                ('require_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='要求完成时间')),
                ('standard', models.CharField(blank=True, max_length=20, null=True, verbose_name='规格')),
                ('nums', models.IntegerField(verbose_name='数量')),
                ('unit', models.CharField(blank=True, max_length=20, null=True, verbose_name='单位')),
                ('adv_com_name', models.CharField(max_length=30, verbose_name='广告公司名称')),
                ('adv_com_contact', models.CharField(blank=True, max_length=20, null=True, verbose_name='广告公司联系人')),
                ('adv_com_mobile', models.CharField(max_length=11, verbose_name='广告公司联系方式')),
                ('cost', models.FloatField(verbose_name='费用')),
                ('make_method', models.CharField(max_length=20, verbose_name='制作方式')),
            ],
            options={
                'verbose_name': '宣传资料内容',
                'verbose_name_plural': '宣传资料内容',
            },
        ),
        migrations.CreateModel(
            name='ItemMakeCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manual_count', models.IntegerField(default=0, verbose_name='手册')),
                ('adv_count', models.IntegerField(default=0, verbose_name='广告')),
                ('video_count', models.IntegerField(default=0, verbose_name='视频')),
                ('leaflet_count', models.IntegerField(default=0, verbose_name='单张')),
                ('other_count', models.IntegerField(default=0, verbose_name='其他')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '宣传物资领用统计',
                'verbose_name_plural': '宣传物资领用统计',
            },
        ),
        migrations.CreateModel(
            name='ItemReceiveCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manual_count', models.IntegerField(default=0, verbose_name='手册')),
                ('badge_count', models.IntegerField(default=0, verbose_name='胸章')),
                ('pendant_count', models.IntegerField(default=0, verbose_name='吊坠')),
                ('ticket_count', models.IntegerField(default=0, verbose_name='电影票')),
                ('other_count', models.IntegerField(default=0, verbose_name='其他')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '宣传物资领用统计',
                'verbose_name_plural': '宣传物资领用统计',
            },
        ),
        migrations.CreateModel(
            name='ItemsMake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.CharField(max_length=200, verbose_name='备注')),
                ('file', models.FileField(blank=True, default='', null=True, upload_to='xc/files/%Y/%m', verbose_name='附件')),
                ('sum_cost', models.FloatField(verbose_name='总费用')),
                ('main', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='xuanchuan.DraftBase', verbose_name='基础信息')),
            ],
            options={
                'verbose_name': '宣传资料制作',
                'verbose_name_plural': '宣传资料制作',
            },
        ),
        migrations.CreateModel(
            name='ItemsReceive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.CharField(max_length=200, verbose_name='备注')),
                ('file', models.FileField(blank=True, default='', null=True, upload_to='xc/files/%Y/%m', verbose_name='附件')),
                ('main', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='xuanchuan.DraftBase', verbose_name='基础信息')),
            ],
            options={
                'verbose_name': '宣传资料制作',
                'verbose_name_plural': '宣传资料制作',
            },
        ),
        migrations.CreateModel(
            name='MessageDraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(default='', max_length=20, verbose_name='开始时间')),
                ('end_time', models.CharField(default='', max_length=20, verbose_name='结束时间')),
                ('content', models.TextField(max_length=500, verbose_name='内容')),
                ('remark', models.CharField(max_length=200, verbose_name='备注')),
                ('file', models.FileField(blank=True, default='', null=True, upload_to='xc/files/%Y/%m', verbose_name='附件')),
                ('category', models.ManyToManyField(to='xuanchuan.Category', verbose_name='类型')),
                ('main', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='xuanchuan.DraftBase', verbose_name='基础信息')),
            ],
            options={
                'verbose_name': '宣传信息起草表',
                'verbose_name_plural': '宣传信息起草表',
            },
        ),
        migrations.CreateModel(
            name='NeedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='宣传品名称')),
                ('unit', models.CharField(default='', max_length=20, verbose_name='单位')),
                ('nums', models.IntegerField(default=0, verbose_name='数量')),
                ('remark', models.CharField(blank=True, max_length=50, null=True, verbose_name='备注')),
                ('use_method', models.CharField(blank=True, max_length=20, null=True, verbose_name='使用方向')),
                ('lis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xuanchuan.ItemsReceive', verbose_name='宣传资料领用表')),
            ],
            options={
                'verbose_name': '需要领用的宣传资料',
                'verbose_name_plural': '需要领用的宣传资料',
            },
        ),
        migrations.CreateModel(
            name='ObjMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='媒体对象')),
            ],
            options={
                'verbose_name': '媒体对象',
                'verbose_name_plural': '媒体对象',
            },
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100, verbose_name='意见')),
                ('leader', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='领导')),
            ],
            options={
                'verbose_name': '意见',
                'verbose_name_plural': '意见',
            },
        ),
        migrations.AddField(
            model_name='messagedraft',
            name='media',
            field=models.ManyToManyField(to='xuanchuan.ObjMedia', verbose_name='媒体对象'),
        ),
        migrations.AddField(
            model_name='messagedraft',
            name='opinion',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='xuanchuan.Opinion', verbose_name='领导意见'),
        ),
        migrations.AddField(
            model_name='itemsreceive',
            name='opinion',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='xuanchuan.Opinion', verbose_name='领导意见'),
        ),
        migrations.AddField(
            model_name='itemsmake',
            name='opinion',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='xuanchuan.Opinion', verbose_name='领导意见'),
        ),
        migrations.AddField(
            model_name='itemmake',
            name='lis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xuanchuan.ItemsMake', verbose_name='宣传资料制作表'),
        ),
    ]
