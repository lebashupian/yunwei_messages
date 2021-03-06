# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-15 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='备份表',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('时间', models.CharField(blank=True, max_length=50, verbose_name='备注： 消息时间')),
                ('来源', models.CharField(max_length=20, verbose_name='备注： 来自哪个主机ip')),
                ('备份文件', models.CharField(default='', max_length=2048, verbose_name='备注： 来自哪个文件')),
                ('备份状态', models.CharField(default='N', max_length=20, verbose_name='备注：是否被确认')),
            ],
        ),
    ]
