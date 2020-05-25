#coding:utf8
import os

def ls(dir):
    if not os.path.exists(dir):
        print('文件不存在')
        return None
    items = os.listdir(dir)
    for item in items:
        if os.path.isdir(os.path.abspath(dir)+item):
            print(item+'/')
        else:
            print(item)

ls('/ls')