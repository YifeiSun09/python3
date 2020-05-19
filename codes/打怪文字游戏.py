from random import random
messages = {
    'intro':[
        "介绍文字",
    ],
    'user_info':'玩家:%s\t金币:%d\t血量:(%d/%d)\t攻击力:%d\t防御力:%d\t\n等级(exp:%d):%d\t下一等级(exp:%d):%d',
    'menu_fighting': '请选择接下来需要进行的动作(1:攻击 2:逃跑 3:治疗):',
    'fight_over':'战斗结束,击败%s,获得%d点经验,%d金币',
    'level_up':'%s升级,当前等级:%d',
    'defeat': '十分遗憾,玩家被%s杀死!',
    'game_again': '是否重新开始游戏(1:是 2:否)? ',
    'game_over': '恭喜你,击败了大boss.',
    'shop_menu': '请选择你的动作:\n1. 购买商品\n2. 出售商品',
    'shop_top': '====下面是店铺中可以买到的商品===',
    'item_info_name': '商品\t类型\t血量\t攻击\t防御', #商品头部信息
    'item_info': '%s\t%s\t%d\t%d\t%d',               #商品信息
    'item_menu_buy': '请选择需要购买的商品:',         #商品
    'item_menu_buy_num': '请选择数量:',               #商品数量
}

# 获取对应等级需要的经验值
def get_level_exp(level):
    return int(10 * 1.2 ** (level - 1))

# 获取当前等级
def get_level(exp):
    level = 1
    
    while exp >= get_level_exp(level):
        exp = exp - get_level_exp(level)
        level = level + 1
    return level,exp #返回当前等级,及在当前等级拥有的经验值

# 商品属性
# type: 1:普通商品,2:武器,3:护具,4:特殊商品
objects = [
    {"type":1,"name":"补血草","attack":0,"hp":10,"defense":0,"price":10},
    {"type":1,"name":"人参","attack":10,"hp":50,"defense":10,"price":100},
    {"type":2,"name":"木棍","attack":2,"hp":0,"defense":0,"price":1},
    {"type":2,"name":"利剑","attack":30,"hp":0,"defense":-5,"price":120},
    {"type":3,"name":"布衣","attack":0,"hp":0,"defense":5,"price":1},
    {"type":3,"name":"护甲","attack":0,"hp":0,"defense":20,"price":120},
]

# 怪物(下标: 0:普通怪物 1:小关主 2:大boss)
monsters = [
    [
        {"name":"巨蚁","hp":10,"attack":8,"defense":10,"exp":3,"money":3},
        {"name":"变异蜂","hp":12,"attack":10,"defense":10,"exp":4,"money":5},
    ],
    [
        {"type":2,"name":"关主1","hp":50,"attack":12,"defense":30,"exp":20,"money":20},
    ],
    [
        {"type":2,"name":"关主1","hp":20,"attack":30,"defense":80,"exp":5,"money":5},
    ]
]

# 玩家属性
user = {
    'name' : 'Francis',     # 名称
    'hp': 100,              # 血量
    'attack': 40,           # 攻击
    'defense': 40,          # 防御力
    'level': 1,             # 等级
    'exp': 0,               # 经验值
    'events': 0,            # 遭遇的事件数
    'has': {
        "armor": None,      # 护甲id
        "weapon": None,     # 武器id
    },
    'objects': {            # 物品id,数量
        2:1,
        4:1,
    }
}

# 处理指定下标的数据
def output(idx):
    global messages
    msg = messages[idx]
    if isinstance(msg,str):
        print(message)
    else:
        for i in msg:
            print(i)

# 伤害计算方式:(攻击-防御) < 0 ? 0 : (攻击-防御) + 1
# a攻击b,成功返回True,否则返回False
def fight(A,B): # A attack B
    res = A.attack - B.defense
    gain = int(random() * (abs(res) + 3))
    if res < 0:
        res = 0
    res = res + gain
    if res >= B.HP:
        B.HP = 0
        return True
    B.HP = B.HP - res # 减掉伤害值
    return False

def getEvent():
    global user,monsters
    n = 100 * random()
    if n < 40: # 40%的概率碰到小怪
        user.events = user.events + 1
        idx = 0
    elif user.events > 20 and n < 55: # 15%的概率碰到关主
        idx = 1
    elif user.events > 60: # 5%的概率遇到大boss
        idx = 2
    else:
        return None
    m = monsters[idx]
    idx = int(random()*len(m))
    monster = m[idx] # 随机获取一个元素
    # 返回一个对象
    return {"type":monster.type,"name":monster.name,"hp":monster.hp,"attack":monster.attack,"defense":monster.defense,"exp":monster.exp,"money":monster.money}

def intro():
    output('intro')

def menu():
    print('')

print(get_level(9))