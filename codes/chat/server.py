#coding:utf-8
import threading
import time
import socket
import atexit
import json

clients = [] # 所有的客户端列表

class Client:
    def __init__(self,sock,addr,name):
        self.sock = sock
        self.addr = addr
        self.name = name

    def close(self):
        self.sock.close()

def onExit(client):
    server.close() # 关闭服务端

def other_clients(client):
    global clients
    return [c for c in clients if c != client ]

# 转发给其他的客户端
def send_to_clients(clients,data):
    for client in clients:
        client.sock.send(data.encode('utf-8'))

def make_msg(**kw):
    return json.dumps(kw)

def logout(client,addr):
    if not client:
        return False
    global clients
    print('%s退出' % client.name)
    clients = other_clients(client)
    send_to_clients(clients,make_msg(name="system",msg=('%s退出' % client.name)))
    client.close()
    return True

# 处理客户端请求
def handle(client,addr):
    cur = None
    try:
        while True:
            data = client.recv(1024).decode('utf-8').strip()
            if data == 'exit':
                logout(cur,addr)
                break

            datas = json.loads(data)

            if 'name' in datas and 'login' in datas:
                cur = Client(client,addr,datas['name']) # 当前客户端
                print('%s上线' % datas['name'])
                send_to_clients(clients,make_msg(name="system",msg='%s上线' % cur.name))
                clients.append(cur)
            elif not cur is None and 'name' in datas and 'msg' in datas:
                print(u"%s: %s" % (datas['name'],datas['msg']))
                data = json.dumps({"name":datas['name'],"msg":datas['msg']})
                send_to_clients(other_clients(cur),data)

    except Exception as e:
        logout(cur,addr)

ip = '0.0.0.0'
port = 10086
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 开启socket
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # ip复用
server.bind((ip,port)) # 绑定10086端口
server.listen(5) # 最多处理5个客户端
atexit.register(onExit,server)
print("服务器监听%s:%d" % (ip, port))
try:
    while True:
        client,addr = server.accept() # 监听远程的连接
        threading.Thread(target = handle,args = (client,addr)).start()
except:
    pass