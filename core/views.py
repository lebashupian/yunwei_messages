from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect

from django.db import models
from django.db.models import *

from core.models import user

# Create your views here.
def login(request):
	return render(request,'login.html')

def login_auth(request):
	# import pdb; pdb.set_trace() 
	user_name=request.POST['user_name']
	user_pwd= request.POST['user_pwd']
	try:
		结果 = user.objects.filter(用户名=user_name,密码=user_pwd)
	except Exception as e:
		#import pdb; pdb.set_trace()
		print("\033[33;40m\33[01m",e,"\033[0m");
		return HttpResponse("查询失败");
	if 结果.count() == 1:
		#return HttpResponse("OK");
		request.session['user_name'] = user_name;
		request.session['user_pwd'] = user_pwd;
		return HttpResponseRedirect("/msgs/index/");
	else:
		return HttpResponse("认证失败,对应的数据库条目数量："+str(结果.count()));

def login_out(request):
	request.session.clear()
	#del request.session['user_name']
	#del request.session['user_pwd']
	return HttpResponseRedirect("/core/login/");


	
