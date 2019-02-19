"""yunwei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from msgs import views
from django.conf.urls import include,url
from django.contrib import admin

#特别注意
#正则表达式不搜索GET和POST参数或域名，比如在https://www.example.com/myapp/?page=3的请求中，URLconf将尝试匹配“myapp/” 这部分 。

urlpatterns = [
	url(r'^index/$', views.index, name='msgs_index'),
	url(r'^删除所有/$', views.删除所有, name='删除所有'),
	url(r'^确认/$', views.确认, name='确认'),
	url(r'^删除当前/(\d+)$', views.删除当前, name='删除当前'),
	url(r'^确认当前/', views.确认当前, name='确认当前'),
    url(r'^提交数据/', views.提交数据, name='提交数据'),
    url(r'^postdata/', views.提交数据, name='postdata'),  #功能和“提交数据” 一致，是为了让ruby标准库的url能支持，而做的兼容
    #http://192.168.137.37:8888/msgs/ceshi/2017/05/04443333/
    url(r'^ceshi/([0-9]{4})/([0-9]{2})/([0-9]+)/$',views.URL测试,name='ceshi'),
]
