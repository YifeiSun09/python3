#coding:utf8
#常见摘要算法练习
import hashlib

md5 = hashlib.md5()

md5.update('How to use md5 in python hashlib'.encode('utf8'))

print(md5.hexdigest()) # 转成16进制摘要

# 遇到大块数据的情况，可以分批计算
md5 = hashlib.md5()
block = ['How to use md5 in ','python hashlib']
for i in block:
    md5.update(i.encode('utf8'))
print(md5.hexdigest())

# sha1算法
sha1 = hashlib.sha1()
sha1.update('Hello'.encode('utf8'))
sha1.update(' World!'.encode('utf8'))
print(sha1.hexdigest())

# sha256
sha256 = hashlib.sha256()
sha256.update('Hello World!'.encode('utf8'))
print(sha256.hexdigest())