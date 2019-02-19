from django.contrib import admin
from msgs.models import *
# Register your models here.

@admin.register(消息)
class 消息Admin(admin.ModelAdmin):
	pass