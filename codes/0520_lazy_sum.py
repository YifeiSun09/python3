#coding:utf8

# 用到了闭包
def lazy_sum(*args):
    def sum():
        ax = 0
        for i in args:
            ax = ax + i
        return ax
    return sum

f = lazy_sum(1,3,5,7,9)
print(f)
print(f())