from django.shortcuts import render
from dwebsocket.decorators import accept_websocket
# Create your views here.


@accept_websocket

def test(request):
    if not request.is_websocket():  # 判断是不是websocket连接
        return render('bac')
    else:
        request.websocket.send("ssssssssssssssssssssssssssssss".encode('utf-8'))  # 发送消息到客户端