from random import random

# 描述性的文字，可以替换成自己需要的文字
messages = {
    'intro':[
        "在很久很久以前，有一个王子和一个公主幸福的生活在一起。",
        "突然有一天，邪恶的大魔王看上了公主，趁着王子外出的时候，将公主掳走。",
        "王子回来后发现公主被邪恶的大魔王掳走，非常伤心，为了救回公主",
        "王子踏上了救回公主的行程。。。。。",
        "",
    ],
    'menu':[
        "请选择接下来的操作：",
        "1. 继续前进",
        "2. 进入商店",
        "3. 打开背包",
        "4. 退出游戏",
    ],
    "menu_select": '操作: ',
    'user_info':'玩家:%s\t金币:%d\t血量:(%d/%d)\t攻击力:%d(+%d)\t防御力:%d(+%d)\t\n武器:%s\t护具:%s\t等级(exp:%d):%d\t下一等级(exp:%d):%d',
    'monster_info': '怪物:%s\t攻击:%d\t防御:%d\t血量:%d',
    'fighting': '请选择接下来需要进行的动作(1:攻击 2:逃跑 3:防守 4:打开物品包):',
    'fight_over':'战斗结束,击败%s,获得%d点经验,%d金币',
    'level_up':'******%s升级,当前等级:%d******',
    'defeat': '十分遗憾,玩家被%s杀死!',
    'game_again': '是否重新开始游戏(1:是 2:否)? ',
    'game_over': '恭喜你,击败了大boss.',
    'shop_menu': '请选择你的动作:\n1. 购买商品\n2. 出售商品',
    'shop_top': '====下面是店铺中可以买到的商品===',
    'item_info_name': 'ID\t商品\t\t类型\t\t血量\t攻击\t防御\t价格', #商品头部信息
    'item_info': '%d\t%s\t\t%s\t\t%d\t%d\t%d\t%d',               #商品信息
    'pack_item_info_name': 'ID\t商品\t\t类型\t\t血量\t攻击\t防御\t数量',
    'pack_item_info': '%d\t%s\t\t%s\t\t%d\t%d\t%d\t%d',
    'item_menu_buy': '请选择需要购买的商品:',         #商品
    'item_menu_buy_num': '请选择数量:',               #商品数量
    'user_name': '请给王子起一个名字:',             #王子名称
    'money_not_enough': '金币不足',
    'invalid_choice': '选项无效',
    'buy_success': '购买成功',
    'encounter_with': '遭遇到%s',
    'escape_success': '撤退成功',
    'escape_fail': '撤退失败',
    'use_object': '使用: ',
    'add_to_pack': '将%s加入背包',
    'use_item': '使用%s',
    'equip_weapon': '装备武器:%s',
    'equip_armor': '装备护具:%s',
    'A_attack_B': '%s向%s发起攻击，伤害%d',
    'attack_invalid': '%s向%s发起攻击，但是看起来并没有什么卵用。。。',
}

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

# 商品类型
object_types = {
    1:'普通',
    2:'武器',
    3:'护具',
    4:'特殊',
}

# 怪物(下标: 0:普通怪物 1:小关主 2:大boss)
monsters = [
    # 小怪，可以加入自己设定的角色
    [
        {"name":"巨蚁","hp":10,"attack":20,"defense":10,"exp":3,"money":3,'fail_rate':0.3},
        {"name":"变异蜂","hp":12,"attack":20,"defense":10,"exp":4,"money":5,'fail_rate':0.3},
    ],
    # 小关主，可以加入自己自定义的角色
    [
        {"name":"关主1","hp":50,"attack":12,"defense":30,"exp":20,"money":20,'fail_rate':0.3},
    ],
    # 大boss，可以键入自己自定义的角色，但是玩家只能遇到一个boss
    [
        {"name":"boss","hp":100,"attack":30,"defense":50,"exp":5,"money":5,'fail_rate':0.3},
    ]
]

# 初始化用户信息
def init_user(username = ''):
    return {
        'name' : username,     # 名称
        'hp': 100,              # 血量
        'full_hp': 100,         # 最高血量
        'attack': 40,           # 攻击
        'defense': 20,          # 防御力
        'gain_attack': 0,       # 额外增加攻击力
        'gain_defense': 0,      # 额外增加防御力
        'level': 1,             # 等级
        'exp': 0,               # 经验值
        'events': 0,            # 遭遇的事件数
        'money': 100,             # 金币
        'event': None,          # 当前事件
        'fail_rate':0.1,        # 攻击失败率
        'has': {
            "armor": 2,      # 护甲id
            "weapon": 4,     # 武器id
        },
        'objects': {            # 物品id,数量
        }
    }

# 玩家属性
user = init_user()

# 获取信息
def __(idx,default = None):
    global messages
    if idx in messages:
        return messages[idx]
    return default

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

# 处理指定下标的数据
def output(idx):
    msg = __(idx)
    if isinstance(msg,str):
        print(msg)
    elif isinstance(msg,list):
        for i in msg:
            print(i)

# 伤害计算方式:(攻击-防御) < 0 ? 0 : (攻击-防御) + 1
# a攻击b,成功返回True,否则返回False
def fight(A,B): # A attack B
    if random() < A['fail_rate']: # 10%的概率攻击失败
        print(__('attack_invalid') % (A['name'],B['name']))
        return False
    gain_attack = 0
    gain_defense = 0
    if 'gain_attack' in A:
        gain_attack = A['gain_attack']
    if 'gain_defense' in B:
        gain_defense = B['gain_defense']
    res = A['attack'] + gain_attack - B['defense'] - gain_defense
    gain = int(random() * (abs(res) + 3))
    if res < 0:
        res = 0
    res = res + gain
    if res >= B['hp']:
        print(__('A_attack_B') % (A['name'],B['name'],B['hp']))
        B['hp'] = 0
        return True
    B['hp'] = B['hp'] - res # 减掉伤害值
    print(__('A_attack_B') % (A['name'],B['name'],res))
    return False

# 获取一个事件
def getEvent():
    global user,monsters
    n = 100 * random()

    if n < 40: # 40%的概率碰到小怪
        user['events'] = user['events'] + 1
        type_id = 0
    elif user['events'] > 20 and n < 55: # 15%的概率碰到关主
        type_id = 1
    elif user['events'] > 60 and n < 60: # 5%的概率遇到大boss
        type_id = 2
    else:
        user['event'] = None
        return user['event']
    m = monsters[type_id]
    idx = int(random()*len(m))
    monster = m[idx] # 随机获取一个元素
    # 返回一个对象
    user['event'] = {"type":type_id,"name":monster['name'],"hp":monster['hp'],"attack":monster['attack'],"defense":monster['defense'],"exp":monster['exp'],"money":monster['money'],'fail_rate':monster['fail_rate']}
    return user['event']
#游戏介绍
def intro():
    output('intro')

# 用户信息
def user_info():
    global user,objects
    info = __('user_info')
    level,exp = get_level(user['exp']) # 获取用户等级，当前等级经验
    next_level_exp = get_level_exp(level) # 下一级所需要的经验
    sep = "=" * 80
    gain_attack = 0   # 额外的攻击力
    gain_defense = 0  # 额外的防御力
    weapon_name = ''  # 武器名
    armor_name = ''   # 护具名
    if not user['has']['weapon'] is None:
        weapon = objects[user['has']['weapon']]
        gain_attack = gain_attack + weapon['attack']
        gain_defense = gain_defense + weapon['defense']
        weapon_name = weapon['name']
    if not user['has']['armor'] is None:
        armor = objects[user['has']['armor']]
        gain_attack = gain_attack + armor['attack']
        gain_defense = gain_defense + armor['defense']
        armor_name = armor['name']
    user['gain_attack'] = gain_attack
    user['gain_defense'] = gain_defense
    print(sep)
    print(info %(user['name'],user['money'],user['hp'],user['full_hp'],user['attack']+user['gain_attack'],user['gain_attack'],user['defense']+user['gain_defense'],user['gain_defense'],weapon_name,armor_name,exp,level,next_level_exp - exp,level+1))
    print(sep)

# 选项
def choice(prompt,choices):
    while True:
        sel = input(prompt)
        if isinstance(choices,dict): # 字典
            if sel in choices:
                return choices[sel]()
        elif isinstance(choices,list): # 列表 
            for i in choices:
                if i == sel:
                    return i
        output('invalid_choice')

# 玩家背包加入物品
def add_item(item_id):
    global user,objects
    print(__('add_to_pack'),objects[item_id]['name'])
    if item_id in user['objects']:
        user['objects'][item_id] = user['objects'][item_id] + 1
    else:
        user['objects'][item_id] = 1

# 删除商品
def del_item(item_id):
    global user
    if item_id in user['objects']:
        user['objects'][item_id] = user['objects'][item_id] - 1
        return True
    return False

# 购物
def shopping():
    global objects,user,object_types
    output('shop_top')
    output('item_info_name')
    item_info = __('item_info')
    
    for idx,item in enumerate(objects):
        print(item_info % (idx,item['name'],object_types[item['type']],item['hp'],item['attack'],item['defense'],item['price']))
    while True:
        sel = choice('需要购买的物品ID(q:取消): ',[str(x) for x in range(len(objects))]+['q'])
        # q表示取消
        if sel != 'q':
            idx = int(sel)
            if objects[idx]['price'] > user['money']: # 钱不够
                output('money_not_enough')
                continue
            output('buy_success')
            user['money'] = user['money'] - objects[idx]['price'] # 金币减少
            add_item(idx) # 向背包中加入商品
        break

def menu():
    menu_select = __('menu_select')
    output('menu')
    choice(menu_select,{'1':getEvent,'2':shopping,'3':open_pack,'4':exit})

def escaped(): # 逃跑
    return random() < 0.5 # 50%的几率逃跑成功

def monster_info(monster): # 显示怪物信息
    print(__('monster_info') % (monster['name'],monster['attack'],monster['defense'],monster['hp']))
    print("*"*80)

# 战斗
def battle(monster):
    global user
    print(__('encounter_with') % (monster['name'])) # 遭遇到怪物
    while True:
        user_info() # 显示用户信息
        monster_info(monster)
        sel = choice(__('fighting'),['1','2','3','4']) # 选择
        if sel == '1': # 攻击
            res = fight(user,monster)
            if res == True: # 战斗成功
                print(__('fight_over') %(monster['name'],monster['exp'],monster['money']))
                user['exp'] = user['exp'] + monster['exp']
                user['money'] = user['money'] + monster['money']
                
                level,next_exp = get_level(user['exp'])
                if level > user['level']: # 用户升级
                    gap = user['level'] - level
                    user['attack'] = int(user['attack'] * (1.1 ** gap))
                    user['defense'] = int(user['defense'] * (1.1 ** gap))
                    user['level'] = level
                    print(__('level_up') % (user['name'],user['level']))
                return 1 # 战斗成功
        elif sel == '2': # 逃跑
            if escaped() :
                output('escape_success')
                return 2 # 逃跑成功
            output('escape_fail')
        elif sel == '3': # 防守
            pass
        elif sel == '4': # 打开物品包
            open_pack()
        res = fight(monster,user) # 怪物发起进攻
        if res == True: # 怪物发起进攻并且得到胜利
            print(__('defeat') % monster['name'])
            return -1
# 使用物品
def use(item_id):
    global user,objects
    item_id = int(item_id)
    item = objects[item_id]
    if item_id in user['objects'] and user['objects'][item_id] > 0: # 物品数量大于0
        item_type = item['type']
        if item_type == 1:
            if user['hp'] == user['full_hp']: # 血量已满
                return False # 使用失败
            elif user['hp'] + item['hp'] > user['full_hp']: # 血量加满
                user['hp'] = user['full_hp']
            else:
                user['hp'] = user['hp'] + item['hp'] # 加血
            print(__('use_item')%(item['name']))
        elif item_type == 2:  # 武器
            if not user['has']['weapon'] is None: # 已经有武器，需要将武器放入背包
                add_item(user['has']['weapon'])
            user['has']['weapon'] = item_id # 装备当前物品
            print(__('equip_weapon')%(item['name']))
        elif item_type == 3:  # 护具
            if not user['has']['armor'] is None: # 已经有护具，需要将护具放入背包
                add_item(user['has']['armor'])
            user['has']['armor'] = item_id # 装备当前物品
            print(__('equip_armor')%(item['name']))
        elif item_type == 4:  # 特殊工具
            pass
        user['objects'][item_id] = user['objects'][item_id] - 1 # 物品数量 - 1
        return True
    return False #使用失败

# 打开物品包
def open_pack():
    global user,objects
    output('pack_item_info_name')
    item_info = __('pack_item_info') # 玩家拥有的商品

    for item_id,num in user['objects'].items():
        item = objects[item_id]
        if num > 0: # 只输出拥有的物品
            print(item_info % (item_id,item['name'],object_types[item['type']],item['hp'],item['attack'],item['defense'],num))
    keys = list(user['objects'].keys())
    keys = [str(x) for x in keys if user['objects'][x] > 0]
    sel = choice(__('use_object'),keys + ['q'])
    if sel != 'q': #不为退出
        use(sel) # 使用商品
    

# 开始游戏
def start_game():
    global user
    intro() #介绍
    user['name'] = input(__('user_name')) # 设置用户名
    while True:
        user_info() # 显示用户信息
        menu()
        event = user['event'] # 用户当前遇到的事件
        print(event)
        if isinstance(event,dict): # 遇到怪物
            res = battle(event)
            print("")
            if res == -1: #玩家被击败
                sel = choice(__('game_again'),['1','2'])
                if sel == '1': # 重新开始
                    user = init_user(user['name'])
                else:
                    break #游戏结束
            elif res == 1 and event['type'] == 2: # 击败boss
                output('game_over')
                sel = choice(__('game_again'),['1','2'])
                if sel == '1': # 重新开始
                    user = init_user(user['name'])
                else:
                    break #游戏结束

# 启动游戏
start_game()