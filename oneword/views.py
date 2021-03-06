from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect,HttpRequest
from django.db.models import Avg,Max,Min,Count
from django.db import models
from django.db.models import *
from msgs.models import 消息
from backup.models import 备份表
from oneword.models import 一句话
from core.models import user

#########
# 发送邮件函数
from django.conf import settings
from django.core.mail import send_mail 

# Create your views here.
# 
def index(request):
	print("------------------------------------------------------------------------------------------------")
	功能实现字典={"报警响动":"muted"}
	################################################
	# 特别注意，get方法中的default方法,只是在内存中设置这个变量，并不将默认值写入session
	username = request.session.get('user_name',default='游客')
	userpwd =  request.session.get('user_pwd',default='')

	# 定义是否有新数据输出
	# 首先记录当前的数据库最大行号，记录到session中
	
	from django.db.models import Avg,Max,Min,Count
	一句话表最大行号=一句话.objects.all().filter(关联用户__icontains=username).aggregate(最大值=Max('id'))
	
	#################################################
	# 如果是None做下转换
	if 一句话表最大行号['最大值'] == None:
		一句话表最大行号['最大值'] = 0

	print("数据库查询到的一句话表最大行号",一句话表最大行号)	
	###############################################
	# 写入session，并将最大的行号写入到session
	if not request.session.get('oneword_max_line_no'):
		request.session['oneword_max_line_no'] = {'最大值':一句话表最大行号['最大值']}
	print("session中的oneword行号最大值是",request.session['oneword_max_line_no'])
	##############################################
	if  一句话表最大行号['最大值'] > request.session['oneword_max_line_no']['最大值']:
		request.session['oneword_max_line_no']['最大值'] = 一句话表最大行号['最大值']
		print(request.session['oneword_max_line_no']['最大值'])
		功能实现字典["报警响动"] = ""
		###########发送邮件
		#send_mail('有数据更新', '有数据更新', 'from@abcd.com',['to@abcd.com'], fail_silently=False)

	# 定义报警的声音文件
	if not request.session.get('alert_sound'):
		print("没有找到alert_sound，马上将默认值写入session");
		request.session['alert_sound'] = 'N'

	#初始化，如果session中没有select_param，就设置默认值
	if not request.session.get('select_param'):
		print("没有找到select_param，马上把默认值写入session")
		request.session['select_param'] = 'display_all'

	#request.session.get('select_param',default='display_all')
	print("--------------------------",request.session.__dict__['_session_cache'])

	#print("@@@@@@@@@@@@",request.GET.get("select_param", default='display_all'))
	try:
		select_param=request.GET['select_param']
		#print("GET获取的值是",select_param)
		request.session['select_param'] = select_param;
		#print("修改后的session",request.session.__dict__['_session_cache'])
	except Exception as e:
		pass

	#print(type(request.session));
	#print(dir(request.session));   #列出类方法
	#打印类信息
	#print(request.session.__class__); 
	#打印session的key，你可以在数据库 select session_key from django_session 查到
	#print(request.session._SessionBase__session_key); #
	#session信息，以字典方式给你
	session字典=request.session.__dict__
	#print(session字典);
	#print(session字典['_SessionBase__session_key']);
	#print(session字典['_session_cache']);
	#session的比较
	#print(request.session.__eq__(request.session)); 
	#########################################
	登录字典={'登录用户':username,'登录密码':userpwd}

	#print("--------------------------",request.session.__dict__['_session_cache'])

	display字典={}
	if request.session.get('select_param') == 'display_all':
		limit_num=100000000
		display字典['display_all']='selected = "selected"'
	elif  request.session.get('select_param') == 'display_10':
		limit_num=10
		display字典['display_10']='selected = "selected"'
	elif  request.session.get('select_param') == 'display_50':
		limit_num=50
		display字典['display_50']='selected = "selected"'
	elif  request.session.get('select_param') == 'display_100':
		limit_num=100
		display字典['display_100']='selected = "selected"'
	elif  request.session.get('select_param') == 'display_200':
		limit_num=200
		display字典['display_200']='selected = "selected"'
	else:
		limit_num=0
		display字典['display_all']='selected = "selected"'

	#print(request.session.get('select_param'))
	#print("limit_num:",limit_num)


	一句话数据_可迭代对象=一句话.objects.filter(关联用户__icontains=username).order_by('确认','id').values('id','时间','来源','内容','确认')[0:limit_num]

	print(一句话数据_可迭代对象);

	from datetime import date
	今天=date.today()
	今天=今天.strftime('%Y-%m-%d')
	备份数据_可迭代对象none=备份表.objects.raw('with 消息 as ( select * from backup_备份表 where 备份日期=\''+今天+'\' ) '+
										'select 消息.id,消息.备份文件,消息.备份状态,消息.备份时间,消息.备份来源,消息.确认状态,消息.备份主机,backup_备份项目.备份项目 '+
										'from 消息 right outer join backup_备份项目 on 消息.备份项目=backup_备份项目.备份项目'+
										' where 消息.id is null')

	统计null数据=0
	for i in 备份数据_可迭代对象none:
		统计null数据 += 1
	print(统计null数据)	

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


	#return HttpResponse("index页面"+str(username));
	if username != '游客' and userpwd != '':
		return render(request,'oneword.html',{"一句话数据_可迭代对象":一句话数据_可迭代对象,"display字典":display字典,"功能实现字典":功能实现字典,"css_备份面板":css_备份面板,"css_消息面板":css_消息面板,"css_一句话面板":css_一句话面板})
	else:		
		return HttpResponseRedirect("/core/login/");

	print(session字典['_session_cache']);

def 删除所有(request):
    一句话.objects.all().delete();
    return HttpResponseRedirect("/oneword/index/");

def 删除当前(request,id):
    一句话.objects.filter(id=id).delete();
    return HttpResponseRedirect("/oneword/index/");

def 确认(request):
    一句话.objects.filter(确认='N').update(确认='Y');
    return HttpResponseRedirect("/oneword/index/");


def 确认当前(request):
	id = request.GET["id"]
	一句话.objects.filter(id=id).update(确认='Y');
	return HttpResponseRedirect("/oneword/index/");

def 提交数据(request):
	################################################
	# post方法 提供给ruby post_form 调用
	################################################
	if request.method == 'POST':  
		post_时间   = request.POST['时间']
		post_来源   = request.POST['来源']
		post_内容   = request.POST['内容']
		post_确认   = request.POST['确认']
		post_关联用户   = request.POST['关联用户']
		一句话对象=一句话(时间=post_时间,来源=post_来源,内容=post_内容,确认=post_确认,关联用户=post_关联用户);
		一句话对象.save();
		return HttpResponse("已经提交");
	################################################
	# post方法 提供给浏览器调用
	# http://192.168.137.37:8888/msgs/postdata/?json={ "时间":"2018-10-12 10:10:01" , "来源":"192.168.1.100" ,"文件":"/var/log/messages","消息":"哈哈哈" ,"状态":"N" }
	################################################
	elif request.method == 'GET':
		json字符串 = request.GET["json"];
		import json
		json字典=json.loads(json字符串)
		消息对象=消息(时间=json字典['时间'],来源=json字典['来源'],文件=json字典['文件'],消息=json字典['消息'],状态=json字典['状态']);
		消息对象.save();
		return HttpResponse("已经提交");