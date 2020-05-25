#coding:utf8

from urllib import request

url = request.urlopen('http://www.baidu.com')
content = url.read()
url.close()
print(content)