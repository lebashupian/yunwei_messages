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
from backup import views
from django.conf.urls import include,url
from django.contrib import admin

#特别注意
#正则表达式不搜索GET和POST参数或域名，比如在https://www.example.com/myapp/?page=3的请求中，URLconf将尝试匹配“myapp/” 这部分 。

urlpatterns = [
	url(r'^index/$', views.index, name='backup_index'),
	url(r'^确认当前/', views.确认当前, name='backup_确认当前'),
        url(r'^提交数据/', views.提交数据, name='backup_提交数据'),
        url(r'^postdata/', views.提交数据, name='backup_postdata'),
]
