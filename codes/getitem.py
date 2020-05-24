#coding:utf8

class Fib():
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a,b = b, a + b
        return a

f = Fib()
for i in range(0,50):
    print("[%02d]: %d" % (i, f[i]) )