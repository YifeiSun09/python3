names = ['Michael','Bob','Tracy']

for name in names:
    print(name)

s = 0
for i in range(1,101):
    s += i
print(s)
print(list(range(0,5)))
print(list(range(10)))

print(sum(range(1,101)))

L = ['Bart','Lisa','Adam']
for i in L:
    print('Hello,'+i+'!')

for i in range(100):
    if i == 50:
        break
    print(i)
for i in range(100):
    if i % 2 == 0:
        continue
    print(i)
