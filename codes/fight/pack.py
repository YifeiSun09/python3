#coding:utf8
# 背包类
class Pack:
    # cap: None 无限制
    def __init__(self,cap = None):
        self.room = {}  # 背包空间
        self.cap = cap
    
    # 判断是否存在
    def has(self,item):
        return (idx in self.room and self.room[idx] > 0)

    # 向背包加入元素
    def addItem(self,item_id):
        if self.has(item_id):
            self.room[item_id] = 0 # 初始化背包
        self.room[item_id] += 1 # 背包对应物品+1
    
    # 从背包删除元素
    def delItem(self,item_id):
        if self.has(item_id): # 存在元素
            self.room[item_id] -= 1 # 元素数量-1
            return True
        return False

    # 遍历背包
    def retrieve(self):
        pass