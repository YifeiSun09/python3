#coding:utf8
import importlib
import random
from config import monsters
from config import items
import math
import base.role
import base.player

class Game:
    # 初始化语言
    def __init__(self,lang_name):
        lib = 'config.langs.'+lang_name
        try:
            self.lang = importlib.import_module(lib)
            self.locale = lang_name
            
            self.player = base.player.Player() # 初始化玩家
            self.init_player()

            self.event_cnt = 0 # 初始化事件计数
            self.m1 = 0 # 小怪计数
            self.m2 = 0 # 关主计数
            self.cur_event = None

            self.monsters = []
            for k,v in enumerate(monsters.monsters): # 怪兽
                v['id'] = k
                self.monsters.append(v)
            self.items = [] # 物品
            for k,v in enumerate(items.items):
                v['id'] = k
                self.items.append(v)
        except err:
            print(err)
            print('Load Language '+lib+' Error')

    # 初始化一个玩家
    def init_player(self):
        player = self.player
        player.id = 0
        player.type = 0
        player.hp = 20
        player.attack = 12
        player.defense = 20
        player.exp = 0
        player.level = 1
        player.money = 50
        player.fail_rate = 0.2 # 攻击失败率
        player.is_defense = False
        player.full_hp = 20
        player.speed = 0.05 # 逃跑成功率
        player.full_attack = player.attack
        player.full_defense = player.defense
        player.full_speed = player.speed
        player.gain_attack = 0
        player.gain_defense = 0
        player.gain_speed = 0
        player.equip = {
            "armor": 8,
            "weapon": 4,
            "speed": 11,
        }
        return player

    # 获取翻译信息
    def get_locale(self):
        return self.lang.messages

    # 获取指定的的翻译
    def get(self,idx,wrapper = None,width_limit = None):
        locale = self.get_locale()
        if idx in locale:
            ret = locale[idx]
            l = len(ret) # 字符串长度
            left = 1
            right = 1
            if not wrapper is None and not width_limit is None and l < width_limit:
                lr = len(wrapper)
                if lr > 0:
                    dis = width_limit - l
                    left = int(dis/2 / lr)
                    right = int((dis - left * lr) / lr)
            if isinstance(ret,str) and not wrapper is None:
                return wrapper * left + ret + wrapper * right
            return ret
        return None
    
    # 输出指定下标
    def output(self,idx):
        msg = self.get(idx)
        if not msg is None:
            if isinstance(msg,str):
                print(msg)
            elif isinstance(msg,dict):
                for i in msg:
                    print(msg[i])
            elif isinstance(msg,list):
                for i in msg:
                    print(i)
    
    # 获取物品或者怪物
    def get_object(self,term,item_id,get_name = False,get_type = False):
        if term == 'items':
            obj = self.items
        else:
            obj = self.monsters
        
        if isinstance(item_id,int) and item_id < len(obj):
            itm = obj[item_id].copy() # 复制一个新的对象
            name_id = itm['name']
            type_id = itm['type']
            itms = self.get(term)
            if get_name:
                itm['name'] = itms['name'][name_id]
            if get_type:
                itm['type'] = itms['type'][type_id]
            return itm
        return None

    # 获取元素
    def item(self,item_id,get_name = False,get_type = False):
        return self.get_object('items',item_id,get_name,get_type)

    # 获取怪物对象
    def get_a_monster(self,item_id,get_name = True,get_type = False):
        attrs = self.get_object('monster',item_id,get_name,get_type)
        return self.toMonster(attrs)
    # 获取怪物
    def monster(self,item_id,get_name = False,get_type = False):
        return self.get_object('monster',item_id,get_name,get_type)
    
    # 获取指定类型的关务
    def get_monsters_by_type(self,type,get_name = False,get_type = False):
        ret = []
        for item in filter(lambda obj:obj['type'] == type,self.monsters):
            ret.append(self.monster(item['id'],get_name,get_type))
        return ret

    def all_items(self):
        return self.items

    def all_monsters(self):
        return self.monsters

    # 获取小关主
    def getLevelBoss(self):
        return self.get_monsters_by_type(2)
    
    # dict转对象
    def toMonster(self,attrs):
        if not isinstance(attrs,dict) or attrs is None:
            return None
        monster = base.role.Role()
        monster.id = attrs['id']
        monster.name = attrs['name']
        monster.type = attrs['type']
        monster.attack = attrs['attack']
        monster.defense = attrs['defense']
        monster.exp = attrs['exp']
        monster.hp = attrs['hp']
        monster.fail_rate = attrs['fail_rate']
        monster.money = attrs['money']
        return monster

    # game_mode:(0关主随机，1关主顺序)
    def event(self,game_mode = 0):
        rnd = random.random()
        self.event_cnt += 1
        self.cur_event = None
        if rnd < 1: # 40%的概率碰到小怪
            monster0 = self.get_monsters_by_type(0,True)
            self.m1 += 1
            self.cur_event = random.choice(monster0)
        elif rnd < 0.45 and (self.event_cnt >= 20 or self.m1 > 10): # 15%的概率碰到关主
            idx = self.m2
            self.m2 += 1
            monster1 = self.get_monsters_by_type(1,True)
            cnt = len(monster1)
            if game_mode == 1: # 顺序模式
                return monster1[idx]
            self.cur_event = random.choice(monster1)
        elif rnd < 0.5 and self.m2 > 5: # 5%的概率碰到大佬怪
            monster2 = self.get_monsters_by_type(2,True)
            self.cur_event = random.choice(monster2)
        return self.cur_event

    # 介绍
    def intro(self):
        self.output('intro')

    # 选项卡
    def choice(self,prompt,choices = [],middleware = None,can_quit = True):
        while True:
            sel = input(prompt)
            if choices == []:
                return sel
            if can_quit and sel == 'q': # 取消操作
                break
            # 中间件函数处理
            if not middleware is None:
                try:
                    sel = middleware(sel)
                except:
                    pass
            if isinstance(choices,list):
                for i in choices:
                    if i == sel:
                        return sel
            elif isinstance(choices,dict):
                for i in choices:
                    if i == sel:
                        return choices[i]()
            print(self.get('invalid_choice'))
    
    # 商店商品列表
    def shop_items_list(self):
        print(self.get('shop_top','=',70))
        print(self.get('item_info_name'))
        print('='*83)
        for item in self.items:
            item = self.item(item['id'],True,True)
            print(self.get('item_info').format(id=item['id'],item_name=item['name'],item_type=item['type'],hp=item['hp'],attack=item['attack'],defense=item['defense'],speed=item['speed'],price=item['price']))
        print('='*83)
        while True:
            print(self.get('money_owned').format(money=self.player.money))
            item_id = self.choice(self.get('item_menu_buy'),list(range(len(self.items))),int)
            if item_id == None:
                break
            num = self.choice(self.get('input_num'))
            if num == None:
                break
            
            item_id = int(item_id)
            num = int(num)
            item = self.item(item_id)
            if item['price'] * num <= self.player.money:
                self.player.money -= num * item['price'] # 减掉金币
                self.player.pack[0].add_item(item_id,num) # 购入数目
                print(self.get('buy_success'))
                break
            else:
                print(self.get('money_not_enough'))

    # 顶部状态栏
    def status_bar(self):
        user = self.player
        level_info = user.level_info # 等级信息
        armor = ('' if user.equip['armor'] is None else self.item(user.equip['armor'],True)['name'])
        weapon = ('' if user.equip['weapon'] is None else self.item(user.equip['weapon'],True)['name'])
        speed = ('' if user.equip['speed'] is None else self.item(user.equip['speed'],True)['name'])
        star_nums = 88
        print('*'*star_nums)
        print(self.get('user_info').format(user_name=user.name,money=user.money,hp=user.hp,full_hp=user.full_hp,attack=user.attack,gain_attack=user.gain_attack,defense=user.defense,gain_defense=user.gain_defense,weapon=weapon,armor=armor,speed=speed,exp=level_info['exp'],level=level_info['level'],next_exp=level_info['next_exp'],next_level=level_info['next_level']))
        # user.enemy = self.get_a_monster(0)
        print('*'*star_nums)
        if not user.enemy is None: # 存在敌人
            monster = user.enemy
            print(self.get('monster_info').format(monster_name=monster.name,hp=monster.hp,attack=monster.attack,defense=monster.defense))
            print('*'*star_nums)
    # 启动游戏
    def start(self,show_intro = False):
        if show_intro: # 显示介绍
            self.intro()
        
        self.player.name = self.choice(self.get('user_name'))
    
    # 显示状态界面
    def equips_list(self):
        print(self.get('equip_page_title','*'*26).format(user_name=self.player.name))
        print(self.get('equip_item_info_name'))
        print('*'*69)
        equip = self.player.equip.items()
        eqs = []
        for idx in equip:
            item_id = equip[idx]
            if not item_id is None: # 存在该装备
                item = self.item(item_id,True,True)
                eqs.append(item_id)
                print(self.get('equip_item_info').format(id = item['id'],item_name = item['name'],item_type = item['type'],hp = item['hp'],attack = item['attack'],defense = item['defense'],speed = item['speed']))
        print('*'*69)
        sel = self.choice(self.get('unload_prompt'),eqs,int)

    # 显示背包
    def pack_list(self):
        print(self.get('pack_page_title','*'*32).format(user_name=self.player.name))
        print(self.get('pack_item_info_name'))
        print('*'*78)
        pack = self.player.pack[0].items
        ids = sorted(pack.keys())
        eqs = []
        # 背包为空时输出
        if len(ids) == 0:
            print(self.get('empty_pack'))
        for i in ids:
            item_id = i
            total = pack[i]
            item = self.item(item_id,True,True)
            eqs.append(item_id)
            print(self.get('pack_item_info').format(id = item['id'],item_name = item['name'],item_type = item['type'],hp = item['hp'],attack = item['attack'],defense = item['defense'],speed = item['speed'],num = total))
        print('*'*80)
        sel = self.choice(self.get('use_object'),eqs,int)

        if sel != 'q' and not sel is None:
            item_id = int(sel)
            self.player.pack[0].del_item(item_id) # 使用1个
    # 清屏
    def clear(self,pause = False):
        if pause:
            input('')
        print('\033c')

    # A fight B
    def fight(self,A,B):
        if A.is_monster:
            a_attack = A.attack
            b_defense = B.defense + B.gain_defense
            if B.is_defense: # 防守
                a_attack = int(a_attack / 2) # 伤害减半
        else:
            a_attack = A.attack + A.gain_attack
            b_defense = B.defense
        hurt = int(a_attack * a_attack / (a_attack + b_defense) + 3 * random.random())
        print(self.get('A_attack_B').format(player_a=A.name,player_b=B.name,hurt=hurt))
        if B.hp <= hurt: # hp为0
            B.hp = 0
            return True
        B.hp -= hurt
        return False
    
    # 逃跑逻辑
    def escape(self):
        return (self.player.speed + self.player.gain_speed) > random.random()
    
    # 战斗
    def battle(self,monster):
        # 设定敌人标志
        self.player.enemy = monster
        if monster is None:
            return False
        encounter_with_showed = False
        player = self.player
        monster = self.player.enemy
        while True:
            self.clear()
            self.status_bar()
            if not encounter_with_showed:
                print(self.get('encounter_with','+++',40).format(monster_name=monster.name))
                print('')
                encounter_with_showed = True
            self.player.is_defense = False # 清除防守状态
            sel = self.choice(self.get('fighting'),['1','2','3','4'],None,False) # 禁用q
            if sel == '1': # fight
                if self.fight(player,monster) == True: # 击败
                    print(self.get('fight_over').format(monster_name=monster.name,exp=monster.exp,money=monster.money))
                    player.exp += monster.exp
                    player.money += monster.money
                    level = player.get_level()
                    level = 10
                    if level > player.level: # 升级
                        print(self.get('level_up').format(user_name=player.name,level=level))
                        player.level = level
                        attack = int(player.attack * 1.1)
                        defense = int(player.defense * 1.1)
                        speed = int(player.speed * 101)/100
                        full_hp = int(player.full_hp * 1.2)
                        player.hp = full_hp # 加满血
                        print(self.get('attr_level_up').format(full_hp=full_hp - player.full_hp,attack=attack - player.attack,defense=defense - player.defense,speed=speed - player.speed))
                        player.attack = attack
                        player.defense = defense
                        player.speed = speed
                        player.full_hp = full_hp
                        player.enemy = self.cur_event = None
                    return True
            elif sel == '2': # escape
                if self.escape():
                    self.output('escape_success')
                    player.enemy = self.cur_event = None
                    return False # 逃跑成功
                self.output('escape_fail') # 逃跑失败
            elif sel == '3': # 防守
                print(self.get('defensing').format(user_name=player.name))
                player.is_defense = True
            elif sel == '4': # 打开物品包
                self.pack_list()
            
            if self.fight(monster,player) == True: # 敌人反击成功
                return False
    # 菜单
    def menu(self):
        self.output('menu')
        sel = self.choice(self.get('menu_select'),{'1':self.event,'2':self.shop_items_list,'3':self.pack_list,'4':exit})
        if sel is None:
            return None
        
        # 存在事件
        if not self.cur_event is None:
            monster = self.toMonster(self.cur_event)
            return self.battle(monster)