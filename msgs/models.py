from django.db import models

import random


# Create your models here.

class 消息管理人(models.Manager):
	def 测试方法(self,测试参数):
		return 测试参数
	def sql查询(self,sql):
		for 结果 in 消息.objects.raw(sql):
			print("sql查询：",结果)

		# 测试1
		# python manages.py shell 
		# from msgs.models import 消息
		# 消息.objects.测试方法("ceshi")
		# 测试2
		# 消息.objects.sql查询('select * from msgs_消息')


class 消息(models.Model):
	#注意，默认值不会体现在数据库表结构中。
	#时间=models.DateTimeField('备注： 消息时间');
	时间=models.CharField('备注： 消息时间',max_length=50,blank=True,null=False);
	来源=models.CharField('备注： 来自哪个主机ip',max_length=20,null=False);
	文件=models.CharField('备注： 来自哪个文件',max_length=2048,null=False,default='');
	消息=models.CharField('备注：消息内容',max_length=2048,null=False,default='');
	状态=models.CharField('备注：是否被确认',max_length=20,null=False,default='N');
	关联用户=models.CharField('备注：消息属于哪些用户的',max_length=2048,null=False,default='admin');

	objects = 消息管理人()

	def 还没有被确认的消息(self):
		 return self.objects.filter(状态='N');

	@classmethod
	def 新建(cls,时间参数,来源参数,消息参数,状态参数):
		实例消息=cls(时间=时间参数,来源=来源参数,消息=消息参数,状态=状态参数)
		#
		#  还可以做其他事情
		#
		return 实例消息

    #测试
    #python manage.py shell
    #from msgs.models import 消息
	#实例=消息.新建('2017-10-12 10:10:01','192.168.0.1','ceshi2','N')
	#实例.save()
	@classmethod
	def 测试插入数据(cls):
		随机数 = random.choice(range(1, 100000000))
		随机数2 = random.choice(range(1, 10))
		实例=消息.新建('2017-10-12 10:10:01','192.168.0.'+str(随机数2),str(随机数),'N')
		实例.save()

	class Meta:
		# 先按时间降序，再按状态升序
		ordering = ["-时间","状态"]   #减号代表降序，没有减号就是升序
		indexes = [
			models.Index(fields=['时间', '来源'],name='时间_来源_idx'),  #联合索引
            models.Index(fields=['状态'], name='状态_idx'),
		]
		unique_together = (("时间", "来源","消息"),)


	#
	# 特例函数，在djangoadmin页面中展示数据的时候，__str__被调用。
	#
	def __str__(self):
		return "{}---{}---{}---{}".format(self.pk, self.来源, self.消息,self.状态)



class 备份主机(models.Model):
	主机ID=models.AutoField(primary_key=True)
	主机IP=models.CharField('IP地址',max_length=20)
	主机类型= (
		('P','x86物理机器'),
		('K','虚拟化kvm'),
		('V','虚拟化vmweare '),
	)
	备份日期=models.DateField('日期')
	备份等级=models.IntegerField('数字等级')
	主机备注=models.TextField('主机备注',max_length=2048,default='空');

	class Meta:
		db_table = '备份主机2' #这里会覆盖class中使用的名称
		#db_tablespace = ''
		get_latest_by = "备份日期"


############################
# 演示外键的设置
############################
class 学生(models.Model):
	姓名 = models.CharField(max_length=100);
class 课程(models.Model):
	科目 = models.CharField(max_length=100);

class 成绩(models.Model):
	姓名 = models.ForeignKey(学生,on_delete=models.CASCADE)
	科目 = models.ForeignKey(课程,on_delete=models.CASCADE)
	成绩 = models.IntegerField('成绩')


############################
# 继承
############################
class 人(models.Model):
	姓名=models.CharField(max_length=50)
	class Meta:
		abstract = True   #如果这里设置是True，这么模型只是用来被继承，而不会真的被创建

class 工程师(人):
	pass

##########################
# 文件存储
###########################
def 自定义路径():
	pass
class 存储(models.Model):
	#pass
	文件id=models.IntegerField('文件ID')
	#file will be uploaded to MEDIA_ROOT/uploads
	上载=models.FileField(upload_to='uploads/')
	#upload = models.FileField(upload_to='uploads/%Y/%m/%d/')




##########################
# 直接执行sql
##########################


##########################
# 事务
##########################
