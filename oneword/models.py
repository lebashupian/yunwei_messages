from django.db import models
import django.utils.timezone as timezone
# Create your models here.

class 一句话(models.Model):
	时间=models.DateTimeField('备注： ',default=timezone.now);
	来源=models.CharField('备注： ',max_length=100,null=False,default='');
	内容=models.CharField('备注： ',max_length=2048,null=False,default='');
	确认=models.CharField('备注：',max_length=20,null=False,default='N');
	关联用户=models.CharField('备注：消息属于哪些用户的',max_length=2048,null=False,default='admin');
