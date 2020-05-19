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