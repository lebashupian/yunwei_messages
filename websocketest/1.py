from websocket import create_connection
ws = create_connection("ws://127.0.0.1:8888/websocketest/index")
ws.send("Hello, World")##发送消息
result = ws.recv()##接收消息
ws.close()
