#coding:utf8

# 基本元素类型
# 0:普通物品 1:武器 2:护具 3:速度 4:特殊
class Item:
    def __init__(self,**kw):
        self.id = (kw['id'] if 'id' in kw else 0)
        self.type = (kw['type'] if 'type' in kw else 0)
        self.name = (kw['name'] if 'name' in kw else '')
        self.hp = (kw['hp'] if 'hp' in kw else 0)
        self.attack = (kw['attack'] if 'attack' in kw else 0)
        self.defense = (kw['defense'] if 'defense' in kw else 0)
        self.price = (kw['price'] if 'price' in kw else 0)
        self.speed = (kw['speed'] if 'speed' in kw else 0)
    
    # 商品回购价格
    @property
    def sale_price(self):
        discount = [0.8,0.5,0.5,0.3,1]
        if isinstance(self.type,int) and self.type >= 0 and self.type <= 4:
            return self.price * discount[self.type]
        return 0