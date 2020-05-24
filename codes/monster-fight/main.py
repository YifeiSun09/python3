#coding:utf8
import game
from base import item
from time import sleep
# 游戏实例
Game = game.Game('zh_CN')

Game.start(True) # 开始
while True:
    Game.clear() # 清屏
    Game.status_bar() # 顶部信息
    Game.menu() # 显示菜单
    sleep(2)
# pack = cur_game.player.pack[0]

