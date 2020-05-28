#coding:utf8
import sys
import socket
import threading
import json

class Client:
    def __init__(self,name,sock,addr):
        self.name = name
        self.sock = sock
        self.addr = addr

class Server:
    def __init__(self,ip = '0.0.0.0',port = 10086):
        self.addr = ip
        self.port = port
        self.clients = []
        sock = self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) # 复用ip
        sock.bind((ip,port))
        sock.listen(10)
        pass

    def make(self,**kw):
        return json.dumps(kw).encode('utf8')

    def expose(self,data):
        return json.loads(data)
    
    # 其他的客户端
    def other_clients(self,client = None):
        if client is None:
            return self.clients
        return [x for x in self.clients if x != client]
    
    def sendto_clients(self,clients,data):
        for client in clients:
            client.sock.send(data)


    def handleClient(self,client,addr):
        name = None
        inst = Client(name,client,addr)
        try:
            while True:
                data = client.recv(1024)
                if data:
                    data = data.decode('utf8').strip()
                    if data == 'exit':
                        print('退出')
                        client.close()
                        sys.exit(0)
                    datas = self.expose(data)
                    others = self.other_clients(inst)
                    if datas['action'] == 'login':
                        name = datas['who'] # 获取用户名
                        inst.name = name
                        self.clients.append(inst) # 向客户端中压入一个数据
                        # 向其他人发送登录通知
                        self.sendto_clients(others,self.make(action='login',who=name))
                    elif not name is None and datas['action'] == 'send_msg' and 'who' in datas:
                        print('%s: %s' %(name,datas['msg']))
                        self.sendto_clients(others,self.make(action='send_msg',who=name,msg=datas['msg']))
        except:
            pass
    def run(self):
        print('Server running at: %s' % self.addr)
        try:
            while True:
                client,addr = self.sock.accept()
                (threading.Thread(target = self.handleClient,args=(client,addr))).start()
        except:
            self.sock.close()
            exit()

Server().run()
