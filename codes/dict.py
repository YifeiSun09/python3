d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
for i in d:
    print(i,d[i])
print('David' in d)

print(d.get('Apple'))
print(d.get('Apple','Not found'))
print(d.get('Tracy'))

print(d.pop('Tracy'))
print(d)
