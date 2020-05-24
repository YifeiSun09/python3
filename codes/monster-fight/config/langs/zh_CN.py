#coding:utf8

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
    # 物品相关的翻译
    'items':{
        # 类型
        'type':{
            0:'普通',
            1:'武器',
            2:'护具',
            3:'提速',
            4:'特殊',
        },
        # 名称
        'name':{
            0:'仙草',
            1:'补血草',
            2:'大补丸',
            3:'回魂丹',
            4:'布鞋',
            5:'皮鞋',
            6:'军皮鞋',
            7:'布衣',
            8:'皮衣',
            9:'军大衣',
            10:'盾牌',
            11:'木棒',
            12:'大刀',
            13:'倚天剑',
            14:'屠龙刀',
            15:'钻石',
        }
    },
    # 怪物相关的翻译
    'monster':{
        'type':{
            0:'普通怪物',
            1:'小关主',
            2:'老怪',
        },
        'name':{
            0:'老虎',
            1:'狮子',
            2:'蜘蛛',
            3:'小魔王',
            4:'小魔王2',
            5:'大魔王',
        }
    },
    "menu_select": '接下来的操作: ',
    'user_info':'玩家:{user_name}\t\t血量:({hp}/{full_hp})\t金币:{money}\t攻击力:{attack}(+{gain_attack})\t防御力:{defense}(+{gain_defense})\t\n武器:{weapon}\t护具:{armor}\t提速:{speed}\t等级(exp:{exp}):{level}\t下一等级(exp:{next_exp}):{next_level}',
    'monster_info': '怪物:{monster_name}\t血量:{hp}\t\t攻击:{attack}\t\t防御:{defense}',
    'fighting': '接下来需要进行的动作(1:攻击 2:逃跑 3:防守 4:打开物品包):',
    'fight_over':'战斗结束,击败{monster_name},获得{exp}点经验,{money}金币',
    'level_up':'{user_name}升级,当前等级:{level}',
    'attr_level_up': '血量:+{full_hp},攻击:+{attack},防御:+{defense},速度:+{speed}',
    'defeat': '十分遗憾,玩家被{monster}杀死!',
    'game_again': '是否重新开始游戏(1:是 2:否)? ',
    'game_over': '恭喜你,击败了大boss.',
    'shop_menu': '请选择你的动作:\n1. 购买商品\n2. 出售商品',
    'shop_top': '下面是店铺中可以买到的商品',
    'item_info_name': 'ID\t物品\t\t类型\t\t血量\t攻击\t防御\t速度\t价格', #商品头部信息
    'item_info': '{id}\t{item_name}\t\t{item_type}\t\t{hp}\t{attack}\t{defense}\t{speed}\t{price}',               #商品信息
    'pack_item_info_name': 'ID\t物品\t\t类型\t\t血量\t攻击\t防御\t速度\t数量',
    'pack_item_info': '{id}\t{item_name}\t\t{item_type}\t\t{hp}\t{attack}\t{defense}\t{speed}\t{num}',
    'equip_item_info_name': 'ID\t物品\t\t类型\t\t血量\t攻击\t防御\t速度',
    'equip_item_info': '{id}\t{item_name}\t\t{item_type}\t\t{hp}\t{attack}\t{defense}\t{speed}',
    'item_menu_buy': '请选择需要购买的商品id(取消:q):',         #商品
    'item_menu_buy_num': '请选择数量(取消:q):',               #商品数量
    'user_name': '请给王子起一个名字:',             #王子名称
    'money_not_enough': '金币不足',
    'invalid_choice': '选项无效',
    'buy_success': '购买成功',
    'encounter_with': '遭遇到{monster_name}',
    'escape_success': '撤退成功',
    'escape_fail': '撤退失败',
    'use_object': '输入id，使用(q:取消): ',
    'add_to_pack': '将{item_name}加入背包',
    'use_item': '使用{item_name}',
    'equip_page_title':'{user_name}的装备',
    'pack_page_title':'{user_name}的背包',
    'equip_weapon': '装备武器:{equip_weapon}',
    'equip_armor': '装备护具:{equip_armor}',
    'equip_speed': '装备鞋子:{equip_speed}',
    'unload_weapon': '卸载武器:{equip_weapon}',
    'unload_armor': '卸载护具:{equip_weapon}',
    'unload_speed': '卸载鞋子:{equip_speed}',
    'unload_prompt': '输入id，卸载装备(q:取消): ',
    'A_attack_B': '{player_a}向{player_b}发起攻击，伤害{hurt}',
    'attack_invalid': '{player_a}向{player_b}发起攻击，但是看起来并没有什么卵用。。。',
    'empty_pack': '背包看起来是空的',
    'input_num': '请输入数目: ',
    'money_owned': '当前金币:{money}',
    'defensing': '{user_name}进行防守',
}