#coding:utf8
# 角色对象
# type:(0:玩家 1:小怪 2:关主 3:boss)
class Role:
    def __init__(self,**kw):
        self.id = kw['id']
        self.type = kw['type']
        self.name = kw['name']
        self.attack = kw['attack']
        self.defense = kw['defense']
        self.money = kw['money']
        self.hp = kw['hp']
        self.exp = kw['exp']
        self.fail_rate = kw['fail_rate']
        self.items = [] # 角色拥有的物品
    
    # 判断是否为玩家
    def isUser(self):
        return self.type == 0
    
    # 判断是否为boss
    def isBoss(self):
        return self.type == 2:

    # 判断是否死亡
    def isDie(self):
        return self.hp <= 0

    # 当前玩家攻击playerB
    def fight(self,playerB):
        pass