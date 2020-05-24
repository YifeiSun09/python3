#coding:utf8
# 角色类
class Role:
    def __init__(self):
        self.id = 0     # 角色id
        self.type = 0   # 角色类型
        self.name = ''  # 角色名称
        self.hp = 0     # 角色血量
        self.attack = 0 # 角色攻击
        self.defense = 0 # 角色防御
        self.exp = 0    # 角色经验
        self.money = 0  # 角色金币
        self.fail_rate = 0 # 攻击失败概率
        self.is_defense = False # 是否存于防御状态
        self.enemy = None # 敌人
        self.is_monster = True

    def infos(self):
        return {
            "id":self.id,
            "type":self.type,
            "name":self.name,
            "hp":self.hp,
            "attack":self.attack,
            "defense":self.defense,
            "exp":self.exp,
            "money":self.money,
            "fail_rate":self.fail_rate,
            "is_defense":self.is_defense,
        }
    # 判断角色是否死亡
    def is_die(self):
        return self.hp <= 0

    # a攻击b
    def attack(self,player_a,player_b):
        if player_a == player_b:
            return False
        player_a.enemy = player_b
        player_b.enemy = player_a
        pass