# 2021/5/28 10:31 HELI
import pygame as pg
import random


# 食物类 用于提升坦克能力
# 继承精灵类 进行重写
class Food(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # 消灭界面上所有敌人
        self.food_boom = './images/food/food_boom.png'
        # 静止界面上所有敌人
        self.food_sleep = './images/food/food_sleep.png'
        # 可以击碎钢板的强力子弹
        self.food_powerbullet = './images/food/food_powerbullet.png'
        # 加固大本营的墙为钢板
        self.food_ironwall = './images/food/food_ironwall.png'
        # 获得一个保护罩
        self.food_protect = './images/food/food_protect.png'
        # 坦克升级
        self.food_level_up = './images/food/food_level_up.png'
        # 坦克生命增加1
        self.food_life = './images/food/food_life.png'
        # 金币加分
        self.food_coin = './images/food/coin.png'
        # 加速器加快坦克速度
        self.food_speedup = './images/food/food_accelerate.png'
        # 传送门
        self.door = './images/food/food_xuan.png'


        # 用一个列表储存所有食物
        self.foods = [self.food_boom, self.food_sleep, self.food_powerbullet, self.food_ironwall, self.food_protect,
                      self.food_level_up, self.food_life, self.food_coin, self.food_speedup,self.door]

        # 食物种类
        self.kind = None
        self.kind2 =None
        # 生成的食物
        self.food = None
        self.food2=None
        # 图像大小
        self.rect = None
        # 是否在界面上出现 默认不出现
        self.being = False
        # 存在的时间 1000ms
        self.time = 1000

    def generate(self):
        # 随机生成食物种类序号0-9
        self.kind = random.randint(0, 9)
        # 根据序号加载食物图像
        if self.kind < 8:
             self.food = pg.image.load(self.foods[self.kind]).convert_alpha()
        else:
            self.food = pg.image.load(self.foods[self.kind2]).convert_alpha()
            self.food2 = pg.image.load(self.foods[self.kind2]).convert_alpha()
       
        # 设置食物大小
        self.rect = self.food.get_rect()
        self.rect.left = random.randint(100, 500)
        self.rect.top = random.randint(100, 500)
        
        x=random.randint(1, 2)
        self.rect2 = self.food.get_rect()
        if x == 1:
            self.rect2.left, self.rect2.top = 3 + 1 * 6 * 24, 53
        else:
            self.rect2.left, self.rect2.top = 3 + 3 * 6 * 24, 53

        # 显示食物
        self.being = True

