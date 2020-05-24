# type:
# 1:普通物品
# 2:武器
# 3:护具
# 4:特殊商品
class Item:
    def __init__(self,**kw):
        self.id = kw['id']
        self.type = kw['type'] # 物品类型
        self.name = kw['name'] # 物品名称
        self.attack = kw['attack'] # 物品攻击
        self.defense = kw['defense'] # 物品防御
        self.speed = kw['speed'] # 增加逃跑概率
        self.price = kw['price'] # 物品价格
        self.desc = kw['desc'] # 物品描述

    # 设置物品价格
    def setPrice(self,price):
        self.price = price
    
    # 获取物品id
    def getId(self):
        return self.id