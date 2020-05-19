#coding=utf8
L = [1,3,5,2,4,6]
res1 = [x*x for x in L]
print(res1)
# 等价于
res1 = []
for x in L:
    res1.append(x*x)
print(res1)

res2 = [x*x for x in L if x % 2 == 0] # 只计算偶数
print(res2)
res2 = []
for x in L:
    if x % 2 == 0:
        res2.append(x*x)
print(res2)

L2 = {"name":"Francis","age":25}
print([str(k)+"="+str(v) for k,v in L2.items()])

# 有else是,需要把if语句前移
# 奇数不变,偶数变平方
res3 = [x*x if x % 2 == 0 else x for x in L]
print(res3)