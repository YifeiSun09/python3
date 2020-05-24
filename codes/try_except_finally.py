#coding:utf8

try:
    print('try...')
    r = 10 / 0
    print('result:',r)
except ZeroDivisionError as e:
    print(e)
finally:
    print('finally')
print('END')

try:
    print('try...')
    r = 10 / int('a')
    print('result:',r)
except ValueError as e:
    print('Value Error:',e)
except ZeroDivisionError as e:
    print('Zero Division Error:',e)
finally:
    print('finally')
print('END')

