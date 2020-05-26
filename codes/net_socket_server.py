#coding:utf8
import socket
import time
import threading

def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!What\'s your name:\n')
    while True:
        try:
            data = sock.recv(1024)
            time.sleep(1)
            if not data or data.decode('utf-8') == 'exit':
                break
            data = data.strip()
            sock.send(('Hello, %s!\n' % data.decode('utf-8')).encode('utf-8'))
            sock.send(b'What\'s your name? ')
        except:
            sock.close()
    sock.close()
    print('Connection from %s closed' % addr)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # ipv4方式打开TCP链接
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(('127.0.0.1',13402)) # 绑定本地的13400端口
s.listen(5) # 最多能同时处理5个连接
print('waiting for connection...')
while True:
    sock,addr = s.accept()
    t = threading.Thread(target=tcplink,args = (sock,addr))
    t.start()