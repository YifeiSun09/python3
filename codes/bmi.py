#coding=utf8
# 计算bmi
print('BMI计算')
height = float(input('请输入你的身高(厘米):'))
weight = float(input('请输入你的体重(千克):'))

bmi = weight/((height / 100)**2)

print('你好,你的BMI为:%.1f' % bmi)
if bmi < 18.5:
    print('有点偏瘦哦!')
elif bmi < 24:
    print('体重正常!')
elif bmi < 27:
    print('有点偏重哦!')
elif bmi < 30:
    print('轻度肥胖,注意饮食!')
elif bmi < 35:
    print('中度肥胖,注意饮食!')
else:
    print('重度肥胖')
