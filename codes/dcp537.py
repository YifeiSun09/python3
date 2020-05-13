#!/usr/bin/env python3
scale = 1000000
arr = [0] * scale
arr[1] = 1
largest = 0
largest_count = 0
def op(n):
    global largest,Dict,arr,scale
    if n < scale and arr[n] > 0:
        res = arr[n]
    else:
        if n % 2 == 0:
            nn = n>>1
        else:
            nn = 3 * n + 1
        res = 1 + op(nn)
        while n < scale:
            arr[n] = res
            n = n << 1

    return res

for i in range(1,1000000):
    res = op(i)
    if res > largest_count:
        largest = i
        largest_count = res
print(largest)
