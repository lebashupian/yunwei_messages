# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 08:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('msgs', '0004_auto_20171211_0647'),
    ]

    operations = [
        migrations.CreateModel(
            name='备份主机',
            fields=[
                ('主机ID', models.AutoField(primary_key=True, serialize=False)),
                ('主机IP', models.CharField(max_length=20, verbose_name='IP地址')),
                ('备份日期', models.DateField(verbose_name='日期')),
                ('备份等级', models.IntegerField(verbose_name='数字等级')),
            ],
            options={
                'db_table': '备份主机2',
                'get_latest_by': '备份日期',
            },
        ),
        migrations.CreateModel(
            name='学生',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('姓名', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='成绩',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('成绩', models.IntegerField(verbose_name='成绩')),
            ],
        ),
        migrations.CreateModel(
            name='课程',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('科目', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='消息',
            options={'ordering': ['-时间', '状态']},
        ),
        migrations.AlterField(
            model_name='消息',
            name='时间',
            field=models.CharField(blank=True, max_length=50, verbose_name='备注： 消息时间'),
        ),
        migrations.AddIndex(
            model_name='消息',
            index=models.Index(fields=['时间', '来源'], name='msgs_消息_时间_9f6243_idx'),
        ),
        migrations.AddIndex(
            model_name='消息',
            index=models.Index(fields=['状态'], name='状态_idx'),
        ),
        migrations.AddField(
            model_name='成绩',
            name='姓名',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msgs.学生'),
        ),
        migrations.AddField(
            model_name='成绩',
            name='科目',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='msgs.课程'),
        ),
    ]