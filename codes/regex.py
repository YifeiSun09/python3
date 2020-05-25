#coding:utf8

import re

def judge(reg,st):
    res = re.match(reg,st)
    print("使用%s匹配%s" % (reg,st))
    if res:
        print('匹配成功')
    else:
        print('匹配失败')
    print()
# 匹配成功返回一个match对象
judge(r'\d+','13400') # 模式判断
judge(r'\d+','apple13400')
# 匹配数字
judge(r'^\d+$','13400') # 判断给定给定字符串是否全为数字
judge(r'^\d+$','apple13400')
# 判断是否为qq号
# qq = int(input('请输入一个QQ号码:'))
qq = '10001'
judge(r'^\d{5,}$',str(qq))

# 判断是否为邮箱
# email = input('请输入一个供验证的邮箱:')
email = '123456@qq.com'
judge(r'^[^@\-_]+@[\w\d_\-]+(\.[\w\d_\-]+)+$',email)
email = '123-456@qq.com'
judge(r'^[^@\-_]+@[\w\d_\-]+(\.[\w\d_\-]+)+$',email)

# 匹配电话11位
tel = '10086'
judge(r'^1\d{2}\-?\d{4}\-?\d{4}',tel)
tel = '15800000000'
judge(r'^1\d{2}\-?\d{4}\-?\d{4}',tel)

## 获取分组信息
info = 'hello! my name is francis. nice to meet you.'
name_re = r'.*my\s+name\s+is\s+(\w+)\..*'
grps = re.match(name_re,info).groups()
name = grps[0] if not grps is None else None
print("user name: %s" % name)


## 拆分字符串
s = 'name:age:height'

# 无区别的情况(理想状态下)
print(s.split(':')) # 普通方式拆分
print(re.split(r':',s)) # 正则方式拆分

# 词法切分
s = 'This is  a   test' # 不规则的情况
print(s.split(' '))
print(re.split(r'\s+',s))

# re表达式预编译
pattern = re.compile(r'\s+')
print(pattern.split(s))

# 获取邮件用户名
def name_of_email(addr):
    pattern1 = re.compile(r'<([^<>]+)>\s*\w+@\w+(?:\.\w+)+')
    pattern2 = re.compile(r'(\w)@\w+(?:\.\w+)+')
    res = pattern1.match(addr)
    if res:
        return res.groups(0)
    res = pattern2.match(addr)
    if res:
        return res.groups(0)
    return None

print(name_of_email('<Tom Paris> tom@voyager.org'))
