#coding:utf8

import itertools

def pi(N):
    li = itertools.count(1,2)
    head_n = itertools.takewhile(lambda x:x < 2 * N,li)
    res = [ 4 * (-1) ** idx / val for idx,val in enumerate(head_n) ]
    return sum(res)

print(pi(10))