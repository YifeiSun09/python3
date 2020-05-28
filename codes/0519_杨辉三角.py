##### 1  
```
def triangles():
    l = []
    while True:
        l = [l[i]+l[i-1] if i > 0 else 1 for i in range(0,len(l))] +[1]
        yield l

n = 0
for i in triangles():
    n = n + 1
    print(i)
    if n == 10:
        break
```
##### 2  
```
def triangles():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0]+L, L+[0])]
```
##### 3  
```
ef triangles():
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]
```
