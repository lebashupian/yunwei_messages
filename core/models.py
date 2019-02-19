from django.db import models

import django.utils.timezone as timezone

# Create your models here.
class user(models.Model):
	#注意，默认值不会体现在数据库表结构中。
	用户名=models.CharField('备注： 用户登录使用的帐号名',max_length=20,null=False);
	密码=models.CharField('备注：登录密码',max_length=20,null=False,default='jack007');
	备注=models.CharField('备注：用户信息备注，比如全名',max_length=1024,null=False,default='');
