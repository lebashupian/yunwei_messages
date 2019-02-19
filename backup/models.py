from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class 备份表(models.Model):
	#注意，默认值不会体现在数据库表结构中。
	#时间=models.DateTimeField('备注： 消息时间');
	备份日期=models.DateField('备注:',default = timezone.now);
	备份时间=models.DateTimeField('备注： ',default=timezone.now);
	备份来源=models.CharField('备注： ',max_length=20,null=False,default='');
	备份主机=models.CharField('备注： ',max_length=2048,null=False,default='');
	备份文件=models.CharField('备注： ',max_length=2048,null=False,default='');
	备份状态=models.CharField('备注：',max_length=20,null=False,default='N');
	确认状态=models.CharField('备注：',max_length=20,null=False,default='N');
	备份项目=models.CharField('用于配置需要备份的项目',max_length=1024,null=True,unique=True);

class 备份项目(models.Model):
	#这个表里面只存需要备份的列表，用于和备份消息进行联查、
	#从而找出是否有有的备份项目没有收到相应的备份信息
	备份项目=models.CharField('用于配置需要备份的项目',max_length=1024,null=True,unique=True);

