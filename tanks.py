import pygame
import random
import scene
from bullet import Bullet
from mine import Mine


# 我方坦克类
class myTank(pygame.sprite.Sprite):
    def __init__(self, player,skin):
        pygame.sprite.Sprite.__init__(self)
        # 玩家编号(1/2)
        self.player = player
        # 不同玩家用不同的坦克(不同等级对应不同的图)
        tank_skin0 =  ['./images/myTank/tank_T1_0.png', './images/myTank/tank_T1_1.png',
                          './images/myTank/tank_T1_2.png']
        tank_skin4 =  ['./images/myTank/tank_T2_0.png', './images/myTank/tank_T2_1.png',
                          './images/myTank/tank_T2_2.png']
        tank_skin2 =  ['./images/myTank/tank_T3_0.png', './images/myTank/tank_T3_1.png',
                          './images/myTank/tank_T3_2.png']
        tank_skin3 =  ['./images/myTank/tank_T4_0.png', './images/myTank/tank_T4_1.png',
                          './images/myTank/tank_T4_2.png']
        tank_skin1 =  ['./images/myTank/tank_T5_0.png', './images/myTank/tank_T5_1.png',
                          './images/myTank/tank_T5_2.png']
        if skin == 0:
            self.tanks = tank_skin0
        elif skin == 1:
            self.tanks = tank_skin1
        elif skin == 2:
            self.tanks = tank_skin2
        elif skin == 3:
            self.tanks = tank_skin3
        elif skin == 4:
            self.tanks = tank_skin4
        else:
            raise ValueError('myTank class -> player value error.')
        # 坦克等级(初始0)
        self.level = 0
        # 载入(两个tank是为了轮子特效)
        self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
        self.tank_0 = self.tank.subsurface((0, 0), (42, 42))
        self.tank_1 = self.tank.subsurface((53, 0), (42, 42))
        self.rect = self.tank_0.get_rect()
        # 坦克游戏时长
        self.time = 0
        # 坦克得分
        self.score = 0
        # 保护罩
        self.protected_mask = pygame.image.load('./images/others/protect.png').convert_alpha()
        self.protected_mask1 = self.protected_mask.subsurface((0, 0), (48, 48))
        self.protected_mask2 = self.protected_mask.subsurface((48, 0), (48, 48))
        # 坦克方向
        self.direction_x, self.direction_y = 0, -1

        # 生成自己的地雷
        self.generate_mine()

        # 不同玩家的出生位置不同
        if player == 1:
            self.rect.left, self.rect.top = 3 + 24 * 8, 3 + 24 * 24 + 50
        elif player == 2:
            self.rect.left, self.rect.top = 3 + 24 * 16, 3 + 24 * 24 + 50
        else:
            raise ValueError('myTank class -> player value error.')
        # 坦克速度
        self.speed = 3
        # 是否存活
        self.being = True
        # 有几条命
        self.life = 3
        # 是否处于保护状态
        self.protected = False
        # 子弹
        self.bullet = Bullet()
        # 是否遇见树
        self.meetTree = False


    def set_mine(self):
        self.mine_obj = Mine()
        self.mine_obj.image_mine = pygame.image.load('./images/others/mine.png')
        self.mine_obj.being = True

    # 射击
    def shoot(self):
        self.bullet.being = True
        self.bullet.turn(self.direction_x, self.direction_y)
        if self.direction_x == 0 and self.direction_y == -1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.bottom = self.rect.top - 1
        elif self.direction_x == 0 and self.direction_y == 1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.top = self.rect.bottom + 1
        elif self.direction_x == -1 and self.direction_y == 0:
            self.bullet.rect.right = self.rect.left - 1
            self.bullet.rect.top = self.rect.top + 20
        elif self.direction_x == 1 and self.direction_y == 0:
            self.bullet.rect.left = self.rect.right + 1
            self.bullet.rect.top = self.rect.top + 20
        else:
            raise ValueError('myTank class -> direction value error.')
        if self.level == 0:
            self.bullet.speed = 8
            self.bullet.stronger = False
        elif self.level == 1:
            self.bullet.speed = 12
            self.bullet.stronger = False
        elif self.level == 2:
            self.bullet.speed = 12
            self.bullet.stronger = True
        elif self.level == 3:
            self.bullet.speed = 16
            self.bullet.stronger = True
        else:
            raise ValueError('myTank class -> level value error.')

    # 放置砖块
    def set_brick(self):
        self.brick_obj = scene.Brick()
        self.brick_obj.brick = pygame.image.load('./images/scene/brick.png')
        self.brick_obj.being = True
        self.brick_obj.turn(self.direction_x, self.direction_y)
        if self.direction_x == 0 and self.direction_y == -1:
            self.brick_obj.rect.left = self.rect.left
            self.brick_obj.rect.bottom = self.rect.top
        elif self.direction_x == 0 and self.direction_y == 1:
            self.brick_obj.rect.left = self.rect.left
            self.brick_obj.rect.top = self.rect.bottom
        elif self.direction_x == -1 and self.direction_y == 0:
            self.brick_obj.rect.right = self.rect.left
            self.brick_obj.rect.top = self.rect.top
        elif self.direction_x == 1 and self.direction_y == 0:
            self.brick_obj.rect.left = self.rect.right
            self.brick_obj.rect.top = self.rect.top

    # 放置树
    def set_tree(self):
        self.tree_obj = scene.Tree()
        self.tree_obj.tree = pygame.image.load('./images/scene/tree1.png')
        self.tree_obj.being = True

        self.tree_obj.rect.left = self.rect.left-20
        self.tree_obj.rect.top = self.rect.top-14
        self.tree_obj.rect.right = self.rect.right-14
        self.tree_obj.rect.bottom = self.rect.bottom-14

    # 等级提升
    def up_level(self):
        if self.level < 3:
            self.level += 1
        try:
            self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
        except:
            self.tank = pygame.image.load(self.tanks[-1]).convert_alpha()

    # 等级降低
    def down_level(self):
        if self.level > 0:
            self.level -= 1
        self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()

    # 向上
    def move_up(self, tankGroup, brickGroup, ironGroup, myhome,riverGroup,treeGroup):
        self.direction_x, self.direction_y = 0, -1
        # 先移动后判断
        self.rect = self.rect.move(self.speed * self.direction_x, self.speed * self.direction_y)
        self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
        self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
        # 是否可以移动
        is_move = True
        # 地图顶端
        if self.rect.top < 53:
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        # 撞石头/钢墙
        if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
                pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        # 撞河流
        if pygame.sprite.spritecollide(self, riverGroup, False, None) or \
                pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False

        # 撞草丛
        if pygame.sprite.spritecollide(self, treeGroup, False, None) :
            # self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            self.meetTree = True
            is_move = True

        # 撞其他坦克
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        # 大本营
        if pygame.sprite.collide_rect(self, myhome):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        return is_move

    # 向下
    def move_down(self, tankGroup, brickGroup, ironGroup,  myhome,riverGroup,treeGroup):
        self.direction_x, self.direction_y = 0, 1
        # 先移动后判断
        self.rect = self.rect.move(self.speed * self.direction_x, self.speed * self.direction_y)
        self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
        self.tank_1 = self.tank.subsurface((48, 48), (48, 48))
        # 是否可以移动
        is_move = True
        # 地图底端
        if self.rect.bottom > 680 - 3:
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        # 撞石头/钢墙
        if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
                pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        # 撞石头/钢墙
        if pygame.sprite.spritecollide(self, riverGroup, False, None) or \
                pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        # 撞草丛
        if pygame.sprite.spritecollide(self, treeGroup, False, None) :
            # self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            self.meetTree = True
            is_move = True
        # 撞其他坦克
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        # 大本营
        if pygame.sprite.collide_rect(self, myhome):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        return is_move

    # 向左
    def move_left(self, tankGroup, brickGroup, ironGroup,  myhome,riverGroup,treeGroup):
        self.direction_x, self.direction_y = -1, 0
        # 先移动后判断
        self.rect = self.rect.move(self.speed * self.direction_x, self.speed * self.direction_y)
        self.tank_0 = self.tank.subsurface((0, 96), (48, 48))
        self.tank_1 = self.tank.subsurface((48, 96), (48, 48))
        # 是否可以移动
        is_move = True
        # 地图左端
        if self.rect.left < 3:
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        # 撞石头/钢墙
        if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
                pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        # 撞河流
        if pygame.sprite.spritecollide(self, riverGroup, False, None) or \
                pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        # 撞草丛
        if pygame.sprite.spritecollide(self, treeGroup, False, None) :
            # self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            self.meetTree = True
            is_move = True
        # 撞其他坦克
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        # 大本营
        if pygame.sprite.collide_rect(self, myhome):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        return is_move

    # 向右
    def move_right(self, tankGroup, brickGroup, ironGroup,  myhome,riverGroup,treeGroup):
        self.direction_x, self.direction_y = 1, 0
        # 先移动后判断
        self.rect = self.rect.move(self.speed * self.direction_x, self.speed * self.direction_y)
        self.tank_0 = self.tank.subsurface((0, 144), (48, 48))
        self.tank_1 = self.tank.subsurface((48, 144), (48, 48))
        # 是否可以移动
        is_move = True
        # 地图右端
        if self.rect.right > 630 - 3:
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        # 撞石头/钢墙
        if pygame.sprite.spritecollide(self, brickGroup, False, None) or \
                pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        # 撞草丛
        if pygame.sprite.spritecollide(self, treeGroup, False, None) :
            # self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            self.meetTree = True
            is_move = True
        # 撞河流
        if pygame.sprite.spritecollide(self, riverGroup, False, None) or \
                pygame.sprite.spritecollide(self, ironGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        # 撞其他坦克
        if pygame.sprite.spritecollide(self, tankGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        # 大本营
        if pygame.sprite.collide_rect(self, myhome):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            is_move = False
        return is_move

    def generate_mine(self):
        self.mines = []
        # self.mines.image_mine
        for i in range(100):
            self.mines.append(Mine())

    # 在屏幕的显示
    # def display(self, screen, delay):
    # 	# 显示地雷
    # 	for mine in self.mines:
    # 		if mine.active:
    # 			screen.blit(mine.image_mine, mine.rect)

    # self.guard.rect.center = self.rect.center1
    # self.guard.display(screen)
    #
    # if self.star_initial.is_completed() is False:
    # 	self.display_star(screen)
    # 	return
    # if delay % 2 == 0:
    # 	self.delayed ^= 1
    # screen.blit(self.cache_image[self.delayed], self.rect)

    def fire_mine(self):
        # 不会和原来的 地雷重合
        all_mines = pygame.sprite.Group()
        for mine in self.mines:
            if mine.active:
                all_mines.add(mine)

        for mine in self.mines:
            if not mine.active:
                mine.rect.center = self.rect.center
                if len(pygame.sprite.spritecollide(mine, all_mines, False)) == 0:
                    mine.active = True
                break

    # 死后重置
    def reset(self):
        self.level = 0
        self.protected = False
        self.tank = pygame.image.load(self.tanks[self.level]).convert_alpha()
        self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
        self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
        self.rect = self.tank_0.get_rect()
        self.direction_x, self.direction_y = 0, -1
        if self.player == 1:
            self.rect.left, self.rect.top = 3 + 24 * 8, 3 + 24 * 24
        elif self.player == 2:
            self.rect.left, self.rect.top = 3 + 24 * 16, 3 + 24 * 24
        else:
            raise ValueError('myTank class -> player value error.')
        self.speed = 3


# 敌方坦克类
class enemyTank(pygame.sprite.Sprite):
    def __init__(self, x=None, kind=None, is_red=None):
        pygame.sprite.Sprite.__init__(self)
        # 用于给刚生成的坦克播放出生特效
        self.born = True
        self.times = 90
        # 坦克的种类编号
        if kind is None:
            self.kind = random.randint(0, 3)
        else:
            self.kind = kind
        # 所有坦克
        self.tanks1 = ['./images/enemyTank/enemy_1_0.png', './images/enemyTank/enemy_1_1.png',
                       './images/enemyTank/enemy_1_2.png', './images/enemyTank/enemy_1_3.png']
        self.tanks2 = ['./images/enemyTank/enemy_2_0.png', './images/enemyTank/enemy_2_1.png',
                       './images/enemyTank/enemy_2_2.png', './images/enemyTank/enemy_2_3.png']
        self.tanks3 = ['./images/enemyTank/enemy_3_0.png', './images/enemyTank/enemy_3_1.png',
                       './images/enemyTank/enemy_3_2.png', './images/enemyTank/enemy_3_3.png']
        self.tanks4 = ['./images/enemyTank/enemy_4_0.png', './images/enemyTank/enemy_4_1.png',
                       './images/enemyTank/enemy_4_2.png', './images/enemyTank/enemy_4_3.png']
        self.tanks = [self.tanks1, self.tanks2, self.tanks3, self.tanks4]
        # 是否携带食物(红色的坦克携带食物)
        if is_red is None:
            self.is_red = random.choice((True, False, False, False, False))
        else:
            self.is_red = is_red
        # 同一种类的坦克具有不同的颜色, 红色的坦克比同类坦克多一点血量
        if self.is_red:
            self.color = 3
        else:
            self.color = random.randint(0, 2)
        # 血量
        self.blood = self.color
        # 载入(两个tank是为了轮子特效)
        self.tank = pygame.image.load(self.tanks[self.kind][self.color]).convert_alpha()
        self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
        self.tank_1 = self.tank.subsurface((48, 48), (48, 48))
        self.rect = self.tank_0.get_rect()
        # 坦克位置
        if x is None:
            self.x = random.randint(0, 2)
        else:
            self.x = x
        self.rect.left, self.rect.top = 3 + self.x * 12 * 24, 53
        # 坦克是否可以行动
        self.can_move = True
        # 坦克速度
        self.speed = max(2 - self.kind, 1)     #old : 0-3  3,2,1,1           now 0-3 2，1，1，1
        # 方向
        self.direction_x, self.direction_y = 0, 1
        # 是否存活
        self.being = True
        # 子弹
        self.bullet = Bullet()
        self.bullet.speed -= 2
        # 是否遇见树
        self.meetTree = False

    # 射击
    def shoot(self):
        self.bullet.being = True
        self.bullet.turn(self.direction_x, self.direction_y)
        if self.direction_x == 0 and self.direction_y == -1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.bottom = self.rect.top - 1
        elif self.direction_x == 0 and self.direction_y == 1:
            self.bullet.rect.left = self.rect.left + 20
            self.bullet.rect.top = self.rect.bottom + 1
        elif self.direction_x == -1 and self.direction_y == 0:
            self.bullet.rect.right = self.rect.left - 1
            self.bullet.rect.top = self.rect.top + 20
        elif self.direction_x == 1 and self.direction_y == 0:
            self.bullet.rect.left = self.rect.right + 1
            self.bullet.rect.top = self.rect.top + 20
        else:
            raise ValueError('enemyTank class -> direction value error.')

    # 随机移动
    def move(self, tankGroup, brickGroup, ironGroup,  myhome,riverGroup,treeGroup):
        self.rect = self.rect.move(self.speed * self.direction_x, self.speed * self.direction_y)
        is_move = True
        if self.direction_x == 0 and self.direction_y == -1:
            self.tank_0 = self.tank.subsurface((0, 0), (48, 48))
            self.tank_1 = self.tank.subsurface((48, 0), (48, 48))
            if self.rect.top < 53:
                self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
                self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
                is_move = False
        elif self.direction_x == 0 and self.direction_y == 1:
            self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
            self.tank_1 = self.tank.subsurface((48, 48), (48, 48))
            if self.rect.bottom > 630 - 3:
                self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
                self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
                is_move = False
        elif self.direction_x == -1 and self.direction_y == 0:
            self.tank_0 = self.tank.subsurface((0, 96), (48, 48))
            self.tank_1 = self.tank.subsurface((48, 96), (48, 48))
            if self.rect.left < 3:
                self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
                self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
                is_move = False
        elif self.direction_x == 1 and self.direction_y == 0:
            self.tank_0 = self.tank.subsurface((0, 144), (48, 48))
            self.tank_1 = self.tank.subsurface((48, 144), (48, 48))
            if self.rect.right > 630 - 3:
                self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
                self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
                is_move = False
        else:
            raise ValueError('enemyTank class -> direction value error.')
        if pygame.sprite.spritecollide(self, brickGroup, False, None) \
                or pygame.sprite.spritecollide(self, ironGroup, False, None) \
                or pygame.sprite.spritecollide(self, tankGroup, False, None)\
                or pygame.sprite.spritecollide(self, riverGroup, False, None):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
            is_move = False

        # 撞草丛
        if pygame.sprite.spritecollide(self, treeGroup, False, None) :
            # self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            self.meetTree = True
            is_move = True

        if pygame.sprite.collide_rect(self, myhome):
            self.rect = self.rect.move(self.speed * -self.direction_x, self.speed * -self.direction_y)
            self.direction_x, self.direction_y = random.choice(([0, 1], [0, -1], [1, 0], [-1, 0]))
            is_move = False
        return is_move

    # 重新载入坦克
    def reload(self):
        self.tank = pygame.image.load(self.tanks[self.kind][self.color]).convert_alpha()
        self.tank_0 = self.tank.subsurface((0, 48), (48, 48))
        self.tank_1 = self.tank.subsurface((48, 48), (48, 48))
