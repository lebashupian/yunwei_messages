# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 02:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('用户名', models.CharField(max_length=20, verbose_name='备注： 用户登录使用的帐号名')),
                ('密码', models.CharField(default='jack007', max_length=20, verbose_name='备注：登录密码')),
                ('用户session', models.CharField(default='', max_length=1024, verbose_name='备注：验证是否登录')),
            ],
        ),
    ]
