#coding:utf8
import role
import pack

class User(Role):
    def __init__(self,**kw):
        self.gain_attack = 0
        self.gain_defense = 0
        self.full_attack = kw['attack']
        self.full_defense = kw['defense']
        self.pack = Pack() # 初始化背包
        self.speed = 0.3 # 逃跑成功率
        self.level = 1 # 等级
    
    # 安装装备
    def equip(self,item):
        pass
    
    # 卸载状态
    def unload(self,item):
        pass

    # 购买装备
    def buy(self,item):
        pass

    # 卖出状态
    def sale(self,item):
        pass
    
    # 获取指定等级需要的积分
    def getLevelExp(self,level):
        pass

    # 获取升到下一级需要的积分
    def getNextLevelExp(self):
        pass

    # 判断玩家等级
    def getExpLevel(self,exp):
        pass

    # 判断是否升级
    def isLevelUp(self):
        if self.getExpLevel(exp) > self.level:
            return True
        return False