from . import role
from . import pack
from . import equip

class Player(role.Role):
    def __init__(self):
        role.Role.__init__(self) # 执行父类的构造器
        self.name = 'Francis'
        self.full_hp = 0
        self.full_attack = 0
        self.full_defense = 0
        self.gain_attack = 0
        self.gain_defense = 0
        self.gain_speed = 0
        self.level = 1
        self.speed = 0
        self.is_monster = False
        # 装备
        self.equip = equip.Equip()
        # 背包
        # 物品id:数目
        self.pack = pack.Pack(),
    # 获取exp对应的等级数
    # 
    def get_level(self,exp = None):
        level = 1
        base_exp = 10
        if exp is None: # 获取默认的经验值
            exp = self.exp
        while exp >= base_exp:
            exp -= base_exp
            base_exp *= 1.1
            level += 1
        return level,int(exp)

    # 达到指定等级需要的积分
    def get_level_exp(self,level):
        return (int(10 * 1.1 ** (level - 2)) if level > 1 else 0)
    
    # 用户信息
    def infos(self):
        infos = role.Role.infos(self) # 载入默认的信息
        infos['speed'] = self.speed
        infos['full_hp'] = self.full_hp
        infos['full_attack'] = self.full_attack
        infos['full_defense'] = self.full_defense
        infos['gain_attack'] = self.gain_attack
        infos['gain_defense'] = self.gain_defense
        infos['gain_speed'] = self.gain_speed
        infos['level'] = self.level
        infos['equip'] = self.equip
        infos['pack'] = self.pack
        return infos
    
    @property
    def level_info(self):
        level,exp = self.get_level()
        next_exp = self.get_level_exp(level + 1) - exp

        return {"level":level,"exp":exp,"next_level":level+1,"next_exp":next_exp}