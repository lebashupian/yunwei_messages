# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-09-28 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0006_auto_20180928_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='备份表',
            name='备份项目',
            field=models.CharField(max_length=1024, null=True, unique=True, verbose_name='用于配置需要备份的项目'),
        ),
        migrations.AlterField(
            model_name='备份项目',
            name='备份项目',
            field=models.CharField(max_length=1024, null=True, unique=True, verbose_name='用于配置需要备份的项目'),
        ),
    ]