#coding:utf8

class Equip:
    def __init__(self,**kw):
        self.armor = (kw['armor'] if 'armor' in kw else None)
        self.weapon = (kw['weapon'] if 'weapon' in kw else None)
        self.speed = (kw['speed'] if 'speed' in kw else None)
    
    def items(self):
        return {"armor":self.armor,"weapon":self.weapon,"speed":self.speed}