#coding:utf8
# 有一个可以返回0/1的硬币,这枚硬币正反面材质不同,返回0或者1的概率并不相同;当然也不会恒返回某一种,利用这枚硬币模拟出材质均匀的硬币效果(0/1概率0.5)
from random import random

# 偏倚的骰子
def toss_baised():
    if random() < 0.9:  # 这里假设p(0)的概率是0.3,p(1) = 0.7
        return 0
    return 1

# 不偏倚的骰子
# p00 = n * n
# p01 = n * (1-n)
# p10 = (1-n) * n
# p11 = (1-n) * (1-n)
# p01 = p10所以可以从这里获取0,1
def toss_unbaised():
    while True:
        x = toss_baised()
        y = toss_baised()
        if x != y: # 这里要求n不为0或者1,否则会出现死循环
            return x

N = 10000
s = 0
for i in range(N):
    s += toss_unbaised()
print(s/N)