#coding:utf8
# 累加器,闭包训练

def createCounter():
    cnt = [0]  # 这里换成数字就会出错
    def counter():
        cnt[0] = cnt[0]+1 # 这里换成数字就会出错
        return cnt[0] # 这里换成数字就会出错
    return counter       

cnt = createCounter()

for i in range(5):
    print(cnt())