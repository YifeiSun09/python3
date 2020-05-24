#coding:utf8

# 名称name|血量hp|攻击力attack|防御力defense|经验值exp|金币money|攻击失败概率fail_rate
monsters = [
    # 小怪
    {"type":0,"name":0,"hp":10,"attack":4,"defense":10,"exp":3,"money":10,"fail_rate":0.3},
    {"type":0,"name":1,"hp":15,"attack":8,"defense":15,"exp":5,"money":25,"fail_rate":0.2},
    {"type":0,"name":2,"hp":20,"attack":10,"defense":15,"exp":10,"money":35,"fail_rate":0.15},
    # 小关主
    {"type":1,"name":3,"hp":120,"attack":30,"defense":20,"exp":30,"money":40,"fail_rate":0.1},
    {"type":1,"name":4,"hp":150,"attack":40,"defense":30,"exp":45,"money":55,"fail_rate":0.1},
    # 大boss
    {"type":2,"name":5,"hp":500,"attack":50,"defense":50,"exp":120,"money":300,"fail_rate":0},
]