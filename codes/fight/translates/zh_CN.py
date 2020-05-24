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
    'user_info':'玩家:{user_name}\t金币:{money}\t血量:({hp}/{full_hp})\t攻击力:{attack}(+{gain_attack})\t防御力:{defense}(+{gain_defense})\t\n武器:{weapon}\t护具:{armor}\t等级(exp:{exp}):{level}\t下一等级(exp:{next_exp}):{next_level}',
    'monster_info': '怪物:{monster_name}\t攻击:{monster_attack}\t防御:{monster_defense}\t血量:{monster_hp}',
    'fighting': '请选择接下来需要进行的动作(1:攻击 2:逃跑 3:防守 4:打开物品包):',
    'fight_over':'战斗结束,击败{monster_name},获得{exp}点经验,{money}金币',
    'level_up':'******{user_name}升级,当前等级:{level}******',
    'defeat': '十分遗憾,玩家被{monster_name}杀死!',
    'game_again': '是否重新开始游戏(1:是 2:否)? ',
    'game_over': '恭喜你,击败了大boss.',
    'shop_menu': '请选择你的动作:\n1. 购买商品\n2. 出售商品',
    'shop_top': '====下面是店铺中可以买到的商品===',
    'item_info_name': 'ID\t商品\t\t类型\t\t血量\t攻击\t防御\t价格', #商品头部信息
    'item_info': '{id}\t{object}\t\t{type}\t\t{hp}\t{attack}\t{defense}\t{price}',               #商品信息
    'pack_item_info_name': 'ID\t商品\t\t类型\t\t血量\t攻击\t防御\t数量',
    'pack_item_info': '{id}\t{object}\t\t{type}\t\t{hp}\t{attack}\t{defense}\t{num}',
    'item_menu_buy': '请选择需要购买的商品:',         #商品
    'item_menu_buy_num': '请选择数量:',               #商品数量
    'user_name': '请给王子起一个名字:',             #王子名称
    'money_not_enough': '金币不足',
    'invalid_choice': '选项无效',
    'buy_success': '购买成功',
    'encounter_with': '遭遇到{monster_name}',
    'escape_success': '撤退成功',
    'escape_fail': '撤退失败',
    'use_object': '使用: ',
    'add_to_pack': '将{item_name}加入背包',
    'use_item': '使用{item_name}',
    'equip_weapon': '装备武器:{item_name}',
    'equip_armor': '装备护具:{item_name}',
    'A_attack_B': '{player_A}向{player_B}发起攻击，伤害{hurt}',
    'attack_invalid': '{player_A}向{player_B}发起攻击，但是看起来并没有什么卵用。。。',
}