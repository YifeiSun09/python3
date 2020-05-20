#coding:utf8

def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        res = func(*args,**kw)
        print('execute end')
        return res
    return wrapper

@log
def test():
    print('Hello,World!')

test()