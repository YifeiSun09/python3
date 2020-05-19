L = [1,3,5,2,4,8]
res = 0
res = reduce(lambda x,y:x+y,map(lambda x:x*x,L))
print(res)