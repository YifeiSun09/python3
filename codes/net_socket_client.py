#coding:utf8

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

url = 'www.sina.com.cn'
s.connect(('%s' % url,80)) # 链接www.sina.com.cn的80端口
s.send(b'GET / HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n' % url)
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close() # 关闭socket
headers,body = data.split('\r\n\r\n') # 分离头与主体
print(body)