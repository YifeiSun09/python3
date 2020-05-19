#coding=utf8
print('鸡兔同笼问题')
try:
    head = int(input("头的数目:"))
    foot = int(input("脚的数目:"))
    cock = (head * 4 - foot) / 2
    rabit = head - cock
    if cock < 0 or rabit < 0 or int(cock) != cock:
        print("数据错误")
    else:
        print("一共有%d只鸡,%d只兔."%(cock,rabit))
except:
    print('数据错误')