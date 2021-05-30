# 场景类(墙、河流、树、冰)
import pygame
import random


# 石头墙
class Brick(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.brick = pygame.image.load('./images/scene/brick.png')
		self.rect = self.brick.get_rect()
		self.being = False


# 钢墙
class Iron(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.iron = pygame.image.load('./images/scene/iron.png')
		self.rect = self.iron.get_rect()
		self.being = False


# 冰
class Ice(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.ice = pygame.image.load('./images/scene/ice.png')
		self.rect = self.ice.get_rect()
		self.being = False


# 河流
class River(pygame.sprite.Sprite):
	def __init__(self, kind=None):
		pygame.sprite.Sprite.__init__(self)
		if kind is None:
			self.kind = random.randint(0, 1)
		self.rivers = ['./images/scene/river1.png', './images/scene/river2.png']
		self.river = pygame.image.load(self.rivers[self.kind])
		self.rect = self.river.get_rect()
		self.being = False


# 树
class Tree(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.tree = pygame.image.load('./images/scene/tree.png')
		self.rect = self.tree.get_rect()
		self.being = False


# 地图
class Map():
	def __init__(self, stage):
		self.brickGroup = pygame.sprite.Group()
		self.ironGroup  = pygame.sprite.Group()
		self.iceGroup = pygame.sprite.Group()
		self.riverGroup = pygame.sprite.Group()
		self.treeGroup = pygame.sprite.Group()
		self.mineGroup = pygame.sprite.Group()
		if stage == 1:
			self.stage1()
		elif stage == 2:
			self.stage2()
		elif stage == 3:
			self.stage3()
		elif stage == 4:
			self.stage4()
		elif stage == 5:
			self.stage5()
	# 关卡一
	def stage1(self):   #y都加50
		for x in [2, 3, 6, 7, 18, 19, 22, 23]:
			for y in [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [10, 11, 14, 15]:
			for y in [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [4, 5, 6, 7, 18, 19, 20, 21]:
			for y in [13, 14]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x in [12, 13]:
			for y in [16, 17]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)
		for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
			self.brick = Brick()
			self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
			self.brick.being = True
			self.brickGroup.add(self.brick)
		for x, y in [(0, 14), (1, 14), (12, 6), (13, 6), (12, 7), (13, 7), (24, 14), (25, 14)]:
			self.iron = Iron()
			self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24+50
			self.iron.being = True
			self.ironGroup.add(self.iron)
	# 关卡二
	def stage2(self):
		for x in [0, 1]:
			for y in [6, 7, 8, 9, 18, 19, 20, 21]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [2, 3]:
			for y in [4, 11, 12, 13]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [4, 5]:
			for y in [2, 11, 12, 13, 14, 15, 16, 17, 18]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [6, 7]:
			for y in [2, 3, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [8, 9, 18, 19]:
			for y in [4, 5, 6, 7, 8, 9, 16, 17, 18]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [11, 14]:
			for y in [16, 17, 23, 24, 25]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [12, 13]:
			for y in [12, 13, 14, 15, 16, 17, 23]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [15, 16, 17]:
			for y in [16, 17, 18]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [18, 19]:
			for y in [12, 13, 14, 15]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [20, 21]:
			for y in [2, 3, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [22, 23, 24]:
			for y in [2, 10, 11, 12, 13]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [24, 25]:
			for y in [18, 19, 20, 21]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x, y in [(1, 4), (1, 5), (1, 10), (1, 11), (3, 2), (3, 3), (7, 8), (7, 9), (6, 24), (6, 25), (10, 16),
					 (10, 17), (14, 18), (20, 8), (20, 9), (20, 24), (20, 24), (20, 25), (22, 14), (22, 15), (22, 16),
					 (22, 17), (24, 8), (24, 9), (24, 3), (25, 4), (25, 5), (25, 6), (25, 7), (25, 8), (25, 9),
					 (25, 10), (25, 11)]:
			self.brick = Brick()
			self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
			self.brick.being = True
			self.brickGroup.add(self.brick)

		for x in [2, 3, 22, 23]:
			for y in [18, 19, 20, 21]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]:
			for y in [20, 21]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 +y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [4, 5, 6, 7, 8, 9, 16, 17, 18, 19, 20, 21, 22, 23]:
			for y in [22, 23]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [10, 11, 16, 17]:
			for y in [6, 7, 8, 9]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [12, 13, 14, 15]:
			for y in [4, 5, 6, 7]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [8, 9, 16, 17]:
			for y in [12, 13, 14, 15]:
				self.iron = Iron()
				self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24+50
				self.iron.being = True
				self.ironGroup.add(self.iron)

		for x in [10, 11, 14, 15]:
			for y in [12, 13]:
				self.iron = Iron()
				self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 +y * 24+50
				self.iron.being = True
				self.ironGroup.add(self.iron)

		for x in [10, 11, 12, 13]:
			for y in [18, 19]:
				self.iron = Iron()
				self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24+50
				self.iron.being = True
				self.ironGroup.add(self.iron)

		for x in [12, 13, 14, 15]:
			for y in [8, 9]:
				self.iron = Iron()
				self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24+50
				self.iron.being = True
				self.ironGroup.add(self.iron)

		for x in [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
			for y in [10, 11]:
				self.river = River()
				self.river.rect.left, self.river.rect.top = 3 + x * 24, 3 + y * 24+50
				self.river.being = True
				self.riverGroup.add(self.river)

	# 关卡3
	def stage3(self):
		for x in [2, 3, 4, 5, 18, 19, 20, 21]:
			for y in [18, 20, 21]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
			for y in [18, 19]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [6, 7, 16, 17]:
			for y in [21, 22]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [10, 11, 12, 13]:
			for y in [20, 21]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [11, 14]:
			for y in [23, 24, 25]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
			for y in [16, 17]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, ]:
			for y in [14, 15]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [4, 5, 16, 17, 18]:
			for y in [12, 13]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [5, 16, 17, 18]:
			for y in [8, 9, 10, 11]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [6, 7, 19, 22]:
			for y in [6, 7, 8]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21]:
			for y in [6, 7]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
			for y in [4, 5]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 +y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [10, 11, 12, 13]:
			for y in [2, 3]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x, y in [(4, 22), (5, 22), (18, 22), (19, 22), (8, 20), (9, 20), (14, 20), (15, 20), (12, 23), (13, 23),
					 (8, 13), (9, 13), (10, 13), (11, 13), (19, 9), (22, 9), (14, 8), (15, 8), (8, 3), (9, 3), (14, 3),
					 (15, 3), (16, 3), (17, 3), (20, 5), (21, 5)]:
			self.brick = Brick()
			self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
			self.brick.being = True
			self.brickGroup.add(self.brick)

		for x in [0, 1]:
			for y in [10, 11]:
				self.river = River()
				self.river.rect.left, self.river.rect.top = 3 + x * 24, 3 + y * 24+50
				self.river.being = True
				self.riverGroup.add(self.river)

		for x in [22, 23, 24, 25]:
			for y in [12, 13]:
				self.river = River()
				self.river.rect.left, self.river.rect.top = 3 + x * 24, 3 +y * 24+50
				self.river.being = True
				self.riverGroup.add(self.river)

		for x in [0, 1]:
			for y in [6, 24, 25]:
				self.iron = Iron()
				self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24+50
				self.iron.being = True
				self.ironGroup.add(self.iron)

		for x in [24, 25]:
			for y in [4, 24, 25]:
				self.iron = Iron()
				self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24+50
				self.iron.being = True
				self.ironGroup.add(self.iron)

		for x in [8, 12]:
			for y in [10, 11]:
				self.iron = Iron()
				self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24+50
				self.iron.being = True
				self.ironGroup.add(self.iron)

		for x in [0, 1]:
			for y in [2, 3, 4, 5, 22, 23]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [2, 3]:
			for y in [0, 1, 2, 3, 24, 25]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [4, 5]:
			for y in [0, 1]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [20, 21]:
			for y in [24, 25]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [22, 23]:
			for y in [0, 1, 22, 23, 24, 25]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [24, 25]:
			for y in [2, 3, 20, 21, 22, 23]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

	# 关卡4
	def stage4(self):
		for x in [0, 2, 4, 21, 23, 25]:
			for y in [22, 23]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 +y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [8, 10, 12, 14, 16]:
			for y in [18, 19]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [9, 11, 13, 15, 17]:
			for y in [16, 17]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [11, 14]:
			for y in [23, 24, 25]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
			for y in [14, 15]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [8, 9, 12, 13, 16, 17]:
			for y in [12, 13]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]:
			for y in [10, 11]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [6, 7, 12, 13, 18, 19]:
			for y in [8, 9]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [6, 7, 8, 9, 12, 13, 16, 17, 18, 19]:
			for y in [6, 7]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]:
			for y in [4, 5]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [10, 11, 12, 13, 14, 15]:
			for y in [2, 3]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x, y in [(8, 3), (9, 3), (16, 3), (17, 3)]:
			self.brick = Brick()
			self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
			self.brick.being = True
			self.brickGroup.add(self.brick)

		# tree
		for x in [0, 1, 24, 25]:
			for y in [2, 3, 4, 5, 10, 11, 12, 13]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [2, 3, 22, 23]:
			for y in [2, 3, 12, 13]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [8, 9, 16, 17]:
			for y in [8, 9]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [10, 11, 14, 15]:
			for y in [6, 7, 8, 9, 12, 13]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		# iron
		for x in [0, 2, 4, 7, 18, 21, 23, 25]:
			for y in [24, 25]:
				self.iron = Iron()
				self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24+50
				self.iron.being = True
				self.ironGroup.add(self.iron)

		for x in [1, 3, 5, 20, 22.24]:
			for y in [20, 21]:
				self.iron = Iron()
				self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 +y * 24+50
				self.iron.being = True
				self.ironGroup.add(self.iron)

		# river
		for x in [0, 1, 2, 3, 4, 5, 20, 21, 22, 23, 24, 25]:
			for y in [14, 15]:
				self.river = River()
				self.river.rect.left, self.river.rect.top = 3 + x * 24, 3 +y * 24+50
				self.river.being = True
				self.riverGroup.add(self.river)

	# 关卡5
	def stage5(self):
		for x in [6, 7, 8, 9, 10, 11, 16, 17]:
			for y in [1, 2, 3]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 +y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [4, 5, 12, 13, 14, 15, 18, 19]:
			for y in [2, 3]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [18, 19, 20, 21]:
			for y in [4, 5]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [20, 21, 22, 23]:
			for y in [6, 7]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [20, 21, 22, 23, 24]:
			for y in [12, 13]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [18, 19, 20, 21, 22, 23, 24]:
			for y in [14, 15]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [0, 1, 6, 7, 8, 9, 16, 17, 18, 19, 20, 21, 22, 23]:
			for y in [16, 17]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]:
			for y in [18, 19]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
			for y in [20, 21]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [4, 5, 16, 17, 18, 19]:
			for y in [22, 23]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x in [11, 14]:
			for y in [23, 24, 25]:
				self.brick = Brick()
				self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 +y * 24+50
				self.brick.being = True
				self.brickGroup.add(self.brick)

		for x, y in [(6, 22), (7, 22), (12, 23), (13, 23), (2, 3), (3, 3)]:
			self.brick = Brick()
			self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24+50
			self.brick.being = True
			self.brickGroup.add(self.brick)

		# tree
		for x in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
			for y in [4, 5]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [0, 1, 2, 3, 16, 17, 18, 19]:
			for y in [6, 7]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [0, 1, 18, 19, 20, 21, 22, 23]:
			for y in [8, 9, 10, 11]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [0, 1, 6, 7, 16, 17, 18, 19]:
			for y in [12, 13]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]:
			for y in [14, 15]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		for x in [2, 3, 4, 5, 10, 11, 12, 13, 14, 15]:
			for y in [16, 17]:
				self.tree = Tree()
				self.tree.rect.left, self.tree.rect.top = 3 + x * 24, 3 + y * 24+50
				self.tree.being = True
				self.treeGroup.add(self.tree)

		# iron
		for x in [4, 5, 10, 11]:
			for y in [8, 9, 10, 11]:
				self.iron = Iron()
				self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24+50
				self.iron.being = True
				self.ironGroup.add(self.iron)

		for x in [24, 25]:
			for y in [18, 19]:
				self.iron = Iron()
				self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24+50
				self.iron.being = True
				self.ironGroup.add(self.iron)

		for x in [0, 1, 6, 7, 24, 25]:
			for y in [20, 21]:
				self.iron = Iron()
				self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 +y * 24+50
				self.iron.being = True
				self.ironGroup.add(self.iron)

		for x in [2, 3, 8, 9, 20, 21, 22, 23, 24, 25]:
			for y in [22, 23]:
				self.iron = Iron()
				self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24+50
				self.iron.being = True
				self.ironGroup.add(self.iron)

	def protect_home(self):
		for x, y in [(11, 23), (12, 23), (13, 23), (14, 23), (11, 24), (14, 24), (11, 25), (14, 25)]:
			self.iron = Iron()
			self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24+50
			self.iron.being = True
			self.ironGroup.add(self.iron)