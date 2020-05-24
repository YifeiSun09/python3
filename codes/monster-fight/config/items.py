#coding:utf8
# 游戏中的物品列表
# type:(0:普通，1:武器，2:护具，3:加速，4:特殊物品)
# 数字格式：type|name_id或name|hp(血量)|attack(攻击影响)|defense(防御影响)|speed(速度影响)|price（价格）
items = [
    # 普通物品
    {'id':0,'type':0,'name':0,'hp':5,'attack':0,'defense':0,'speed':0,'price':5},
    {'id':1,'type':0,'name':1,'hp':12,'attack':0,'defense':0,'speed':0,'price':10},
    {'id':2,'type':0,'name':2,'hp':25,'attack':0,'defense':0,'speed':0,'price':20},
    {'id':3,'type':0,'name':3,'hp':50,'attack':0,'defense':0,'speed':0,'price':45},
    # 武器
    {'id':4,'type':1,'name':11,'hp':0,'attack':10,'defense':0,'speed':0,'price':20},
    {'id':5,'type':1,'name':12,'hp':0,'attack':20,'defense':0,'speed':-0.05,'price':50},
    {'id':6,'type':1,'name':13,'hp':0,'attack':40,'defense':0,'speed':-0.1,'price':120},
    {'id':7,'type':1,'name':14,'hp':0,'attack':60,'defense':-5,'speed':-0.15,'price':160},
    # 护具
    {'id':8,'type':2,'name':7,'hp':0,'attack':0,'defense':30,'speed':0,'price':20},
    {'id':9,'type':2,'name':8,'hp':0,'attack':0,'defense':40,'speed':0,'price':50},
    {'id':10,'type':2,'name':9,'hp':0,'attack':0,'defense':60,'speed':0,'price':100},
    # 提速
    {'id':11,'type':3,'name':4,'hp':0,'attack':0,'defense':2,'speed':0.1,'price':10},
    {'id':12,'type':3,'name':5,'hp':0,'attack':0,'defense':4,'speed':0.3,'price':30},
    {'id':13,'type':3,'name':6,'hp':0,'attack':0,'defense':8,'speed':0.5,'price':50},
    # 特殊物品
    {'id':14,'type':4,'name':15,'hp':0,'attack':0,'defense':0,'speed':0,'price':5000},
]