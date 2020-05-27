#coding:utf8
import json
import socket
import threading
import atexit
import sys,os

class Client:
    def __init__(self):
        self._ip = '118.25.38.204'
        self._port = 10086
        self.name = None
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((self._ip,self._port))
        self.isLogin = False

    def sendMsg(self,msg):
        if not self.isLogin:
            print('请先登录!')
            return False
        data = json.dumps({"name":self.name,"msg":msg})
        self.sock.send(data.encode('utf8'))
        return True

    def login(self,name = None):
        if name is None:
            self.name = input("请输入你的名字:").strip()
        data = json.dumps({"name":self.name,"login":True})
        self.sock.send(data.encode('utf8'))
        self.isLogin = True

    def chat_inline(self):
        while True:
            line = input('[%s] ' % self.name).strip()
            if line == 'exit':
                self.sock.send(b'exit')
                sys.exit(0)
                break
            self.sendMsg(line)

    def run(self):
        self.login() # 登录
        threading.Thread(target = self.chat_inline,args = ()).start()
        try:
            while True:
                data = self.sock.recv(1024)
                if data:
                    data = data.decode('utf8')
                    datas = json.loads(data)
                    print("\r%s: %s" %(datas['name'],datas['msg']))
                    print("[%s] " % self.name,end = '')
                    sys.stdout.flush()
        except SystemExit:
            return False
        except:
            print('Exception')
            self.sock.close()

client = Client()
client.run()

def onExit(client):
    print('退出')
    client.send('exit'.encode('utf8'))
    client.close()

atexit.register(onExit,client.sock)
