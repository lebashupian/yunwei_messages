# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-15 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backup', '0004_备份表_确认状态'),
    ]

    operations = [
        migrations.AddField(
            model_name='备份表',
            name='备份主机',
            field=models.CharField(default='', max_length=2048, verbose_name='备注： '),
        ),
    ]
