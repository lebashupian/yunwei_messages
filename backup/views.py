from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.db.models import Avg,Max,Min,Count
from django.db import models
from django.db.models import *
from backup.models import 备份表
from msgs.models import 消息
from oneword.models import 一句话
from core.models import user

def index(request):
	print("------------------------------------------------------------------------------------------------")
	################################################
	# 特别注意，get方法中的default方法,只是在内存中设置这个变量，并不将默认值写入session
	username = request.session.get('user_name',default='游客')
	userpwd =  request.session.get('user_pwd',default='')

	from datetime import date
	今天=date.today()

	#备份数据_可迭代对象=备份表.objects.all().filter(备份日期=今天).order_by('确认状态').values('id','备份日期','备份时间','备份来源','备份主机','备份文件','备份状态','确认状态')
	

	#今天.strftime('%Y-%m-%d') 是将date类型转化成字符串类型，方便sql字符串拼接
	今天=今天.strftime('%Y-%m-%d')
	
	备份数据_可迭代对象=备份表.objects.raw('with 消息 as ( select * from backup_备份表 where 备份日期=\''+今天+'\' ) '+
										'select 消息.id,消息.备份文件,消息.备份状态,消息.备份时间,消息.备份来源,消息.确认状态,消息.备份主机,backup_备份项目.备份项目 '+
										'from 消息 right outer join backup_备份项目 on 消息.备份项目=backup_备份项目.备份项目'+
										' order by 消息.确认状态 desc')


	备份数据_可迭代对象none=备份表.objects.raw('with 消息 as ( select * from backup_备份表 where 备份日期=\''+今天+'\' ) '+
										'select 消息.id,消息.备份文件,消息.备份状态,消息.备份时间,消息.备份来源,消息.确认状态,消息.备份主机,backup_备份项目.备份项目 '+
										'from 消息 right outer join backup_备份项目 on 消息.备份项目=backup_备份项目.备份项目'+
										' where 消息.id is null')

	统计null数据=0
	for i in 备份数据_可迭代对象none:
		统计null数据 += 1
	print(统计null数据)


	备份未确认=0
	for abcc in 备份数据_可迭代对象:
		print(type(abcc.确认状态))
		print(type(None))
		if type(abcc.确认状态) == type(None) or abcc.确认状态=='N':
			备份未确认 += 1

	备份未确认=备份表.objects.filter(确认状态='N').count() + 统计null数据
	消息未确认=消息.objects.filter(状态='N').count()
	一句话未确认=一句话.objects.filter(确认='N').count()
	if 备份未确认 > 0:
		css_备份面板='未确认'
	else:
		css_备份面板='确认'
	if 消息未确认 > 0:
		css_消息面板='未确认'
	else:
		css_消息面板='确认'
	if 一句话未确认 > 0:
		css_一句话面板='未确认'
	else:
		css_一句话面板='确认'

	if username != '游客' and userpwd != '':
		print(备份数据_可迭代对象)
		for abc in 备份数据_可迭代对象:
			print(type(abc.确认状态))
		return render(request,'backup.html',{"备份数据_可迭代对象":备份数据_可迭代对象,"备份未确认":备份未确认,"css_备份面板":css_备份面板,"css_消息面板":css_消息面板,"css_一句话面板":css_一句话面板})
	else:		
		return HttpResponseRedirect("/core/login/");

def 确认当前(request):
	id = request.GET["id"]
	if id != 'None':
		备份表.objects.filter(id=id).update(确认状态='Y');
	return HttpResponseRedirect("/backup/index/");

def 提交数据(request):
	################################################
	# post方法 提供给ruby post_form 调用
	################################################
	if request.method == 'POST':  
		post_备份日期   = request.POST['备份日期']
		post_备份时间   = request.POST['备份时间']
		post_备份来源   = request.POST['备份来源']
		post_备份主机   = request.POST['备份主机']
		post_备份文件   = request.POST['备份文件']
		post_备份状态   = request.POST['备份状态']
		post_确认状态   = request.POST['确认状态']
		post_备份项目   = request.POST['备份项目']
		备份对象=备份表(备份日期=post_备份日期,备份时间=post_备份时间,备份来源=post_备份来源,备份主机=post_备份主机,备份文件=post_备份文件,备份状态=post_备份状态,确认状态=post_确认状态,备份项目=post_备份项目);
		备份对象.save();
		return HttpResponse("已经提交");
