#coding:utf8

# 背包
class Pack:
    # 背包,默认容量50,None为不限制容量
    def __init__(self,cap = 50):
        self.cap = cap
        self.items = {}
    
    # 加入物品或id
    def add_item(self,item_id,cnt = 1):
        if self.cap is None or len(self.items) + cnt - 1 < self.cap:
            if item_id in self.items:
                self.items[item_id] += cnt
            else:
                self.items[item_id] = cnt
            return True
        return False
    
    # 从背包删除物品
    def del_item(self,item_id,cnt = 1):
        if item_id in self.items:
            # 删除指定数目的元素
            if self.items[item_id] >= cnt:
                self.items[item_id] -= cnt
                return True
        return False