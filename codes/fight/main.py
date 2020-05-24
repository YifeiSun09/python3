# 游戏主文件
import translates.zh_CN as locale
import user
import shop
import util

player = user.User() # 创建一个对象
shop = shop.Shop(items) # 创建商店
util = util.Util()

output('intro') # 显示游戏介绍
# 游戏开始
while True:
    util.choice('',[])