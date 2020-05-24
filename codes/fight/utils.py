from collection import Iterator
from random import random
#工具类
class Utils:
    # 设定区域相关翻译
    def __init__(self,locales):
        self.locales = locales
    
    # 输出指定下标对应的语言
    def output(self,idx,fmt = ()):
        if idx in self.locales:
            msg = self.locales[idx]
            if isinstance(msg,str):
                print(str.format(fmt))
            elif isinstance(msg,list):
                for i in msg:
                    print(i.format(fmt))
            elif isinstance(msg,dict):
                for i in msg:
                    print(msg[i].format(fmt))
        else:
            print(idx)
    
    # 获取对应的翻译
    def getMessage(self,idx):
        if idx in self.locales:
            return self.locales[idx]
        return None # 不存在返回None
    
    # 选择
    def choice(self,msg = '',choices = []):
        choices = filter(lambda x:x != 'q',choices)
        while True:
            sel = input(msg)
            if sel == 'q': # 取消选择
                break
            elif isinstance(choices,dict): # 字典
                if sel in choices:
                    choices[sel]() # 执行对应的函数
                    return sel
            elif isinstance(choices,list): # 列表
                for i in choices:
                    if sel == i:
                        return sel
            output('invalid_choice') # 选择无效

    # 获取一个事件
    def event(self):
        pass