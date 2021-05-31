import sys
import pygame
import scene
import bullet
import food
import tanks
import home
from pygame.locals import *
from Boom import *
# 主函数
from interface import show_switch_stage, show_start_interface, show_select_interface


def main():
	# 初始化
	pygame.init()
	pygame.mixer.init()
	screen = pygame.display.set_mode((630, 680), FULLSCREEN)
	pygame.display.set_caption("坦克大战——哈哈哈")
	#加载字体
	font_bar = pygame.font.Font('./font/simkai.ttf', 630 // 40)
	# 加载图片
	bg_img = pygame.image.load("./images/others/background.png")
	bar_img = pygame.image.load("./images/others/bar_top.png")
	barProgress_img = pygame.image.load("./images/others/bar_progress.png").convert_alpha()
	open_img = pygame.image.load("./images/others/open.png")
	close_img = pygame.image.load("./images/others/close.png")

	# 加载音效
	music = True  #默认播放音乐
	add_sound = pygame.mixer.Sound("./audios/add.wav")
	add_sound.set_volume(1)
	bang_sound = pygame.mixer.Sound("./audios/bang.wav")
	bang_sound.set_volume(1)
	blast_sound = pygame.mixer.Sound("./audios/blast.wav")
	blast_sound.set_volume(1)
	fire_sound = pygame.mixer.Sound("./audios/fire.wav")
	fire_sound.set_volume(1)
	Gunfire_sound = pygame.mixer.Sound("./audios/Gunfire.wav")
	Gunfire_sound.set_volume(1)
	hit_sound = pygame.mixer.Sound("./audios/hit.wav")
	hit_sound.set_volume(1)
	start_sound = pygame.mixer.Sound("./audios/start.wav")
	start_sound.set_volume(1)
	# 开始界面
	num_player = show_start_interface(screen, 630, 680)
	# 播放游戏开始的音乐
	start_sound.play()
	skin=[]
	skin_num1 = show_select_interface(screen, 630, 680, 1)
	skin.append(skin_num1)
	if num_player >1:
		skin_num2 = show_select_interface(screen, 630, 680, 2)
		skin.append(skin_num2)

	# 关卡
	stage =0
	num_stage = 5
	# 游戏是否结束
	is_gameover = False
	# 时钟
	clock = pygame.time.Clock()

	# 主循环
	while not is_gameover:
		# 关卡
		stage += 1
		if stage > num_stage:
			break
		show_switch_stage(screen, 630, 680, stage)
		# 该关卡坦克总数量
		enemytanks_total = min(stage * 18, 80)  #还未出现的总数，会一直减
		enemytanks_all = enemytanks_total   #总数量，常量
		enemytanks_dead = 0  #敌方死亡数量
		# 场上存在的敌方坦克总数量
		enemytanks_now = 0
		# 场上可以存在的敌方坦克总数量
		enemytanks_now_max = min(max(stage * 2, 4), 8)

		# 精灵组
		tanksGroup = pygame.sprite.Group()
		mytanksGroup = pygame.sprite.Group()
		enemytanksGroup = pygame.sprite.Group()
		bulletsGroup = pygame.sprite.Group()
		mybulletsGroup = pygame.sprite.Group()
		enemybulletsGroup = pygame.sprite.Group()
		myfoodsGroup = pygame.sprite.Group()

		# 自定义事件
		# 	-生成敌方坦克事件
		genEnemyEvent = pygame.constants.USEREVENT
		pygame.time.set_timer(genEnemyEvent, 100)
		# 	-敌方坦克静止恢复事件
		recoverEnemyEvent = pygame.constants.USEREVENT
		pygame.time.set_timer(recoverEnemyEvent, 8000)
		# 	-我方坦克无敌恢复事件
		noprotectMytankEvent = pygame.constants.USEREVENT
		pygame.time.set_timer(noprotectMytankEvent, 8000)
		# 关卡地图
		map_stage = scene.Map(stage)
		map_stage.mineGroup = pygame.sprite.Group()
		# 我方坦克
		tank_player1 = tanks.myTank(1)
		tanksGroup.add(tank_player1)
		mytanksGroup.add(tank_player1)
		play1 = font_bar.render(u'P1 S、L', True, (255, 255, 255))
		p1rect = play1.get_rect()
		p1rect.midtop = (830 / 2, 50 / 3.7)
		play1_score = font_bar.render(str(tank_player1.score), True, (255, 255, 255))  #玩家1得分
		p1rect_score = play1_score.get_rect()
		p1rect_score.midtop = (480, 50 / 3.7)
		play1_life = font_bar.render(str(tank_player1.life), True, (255, 255, 255))  # 玩家1生命
		p1rect_life = play1_life.get_rect()
		p1rect_life.midtop = (520, 50 / 3.7)
		if num_player > 1:
			tank_player2 = tanks.myTank(2)
			tanksGroup.add(tank_player2)
			mytanksGroup.add(tank_player2)
			play2 = font_bar.render(u'P2 S、L', True, (255, 255, 255))
			p2rect = play2.get_rect()
			p2rect.midtop = (830 / 2, 50 / 1.6)
			play2_score = font_bar.render(str(tank_player2.score), True, (255, 255, 255)) #玩家2得分
			p2rect_score = play2_score.get_rect()
			p2rect_score.midtop = (480, 50 / 1.6)
			play2_life = font_bar.render(str(tank_player2.life), True, (255, 255, 255))  # 玩家2生命
			p2rect_life = play2_life.get_rect()
			p2rect_life.midtop = (520, 50 / 1.6)
		is_switch_tank = True
		player1_moving = False
		player2_moving = False
		# 为了轮胎的动画效果
		time = 0
		# 敌方坦克
		for i in range(0, 3):
			if enemytanks_total > 0:
				enemytank = tanks.enemyTank(i)
				tanksGroup.add(enemytank)
				enemytanksGroup.add(enemytank)
				enemytanks_now += 1
				enemytanks_total -= 1
		# 大本营
		myhome = home.Home()
		# 出场特效
		appearance_img = pygame.image.load("./images/others/appear.png").convert_alpha()
		appearances = []
		appearances.append(appearance_img.subsurface((0, 0), (48, 48)))
		appearances.append(appearance_img.subsurface((48, 0), (48, 48)))
		appearances.append(appearance_img.subsurface((96, 0), (48, 48)))

		# 爆炸特效
		boom_img = pygame.image.load("./images/others/boom_dynamic.png").convert_alpha()
		boom_imgs = []
		boom_imgs.append(boom_img.subsurface((0, 0),(48, 48)))
		boom_imgs.append(boom_img.subsurface((48, 0), (48, 48)))
		boom_imgs.append(boom_img.subsurface((96, 0), (48, 48)))
		boom_imgs.append(boom_img.subsurface((144, 0), (48, 48)))
		boom_imgs.append(boom_img.subsurface((192, 0), (48, 48)))
		boom_imgs.append(boom_img.subsurface((240, 0), (48, 48)))



		# 关卡主循环
		while True:
			if is_gameover is True:
				break
			if enemytanks_total < 1 and enemytanks_now < 1:
				barProgress_green = barProgress_img.subsurface((0, 0), (250, 24))
				screen.blit(barProgress_green, (60, 17))
				is_gameover = False
				break
			for event in pygame.event.get():
				#鼠标点击音乐图片事件
				if event.type == pygame.MOUSEBUTTONDOWN:
					x, y = event.pos
					if x < 612 and x >580 and y>5 and y < 37:
						if music:
							music = False
							start_sound.stop()
						else:
							music = True
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == genEnemyEvent:
					if enemytanks_total > 0:
						if enemytanks_now < enemytanks_now_max:
							enemytank = tanks.enemyTank()
							if not pygame.sprite.spritecollide(enemytank, tanksGroup, False, None):
								tanksGroup.add(enemytank)
								enemytanksGroup.add(enemytank)
								enemytanks_now += 1
								enemytanks_total -= 1
				if event.type == recoverEnemyEvent:
					for each in enemytanksGroup:
						each.can_move = True
				if event.type == noprotectMytankEvent:
					for each in mytanksGroup:
						mytanksGroup.protected = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
						sys.exit()
			# 检查用户键盘操作
			key_pressed = pygame.key.get_pressed()

			# 玩家一
			# WSAD -> 上下左右
			# 空格键射击
			if key_pressed[pygame.K_w]:
				tanksGroup.remove(tank_player1)
				tank_player1.move_up(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
				tanksGroup.add(tank_player1)
				player1_moving = True
			elif key_pressed[pygame.K_s]:
				tanksGroup.remove(tank_player1)
				tank_player1.move_down(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
				tanksGroup.add(tank_player1)
				player1_moving = True
			elif key_pressed[pygame.K_a]:
				tanksGroup.remove(tank_player1)
				tank_player1.move_left(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
				tanksGroup.add(tank_player1)
				player1_moving = True
			elif key_pressed[pygame.K_d]:
				tanksGroup.remove(tank_player1)
				tank_player1.move_right(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
				tanksGroup.add(tank_player1)
				player1_moving = True
			elif key_pressed[pygame.K_SPACE]:
				if not tank_player1.bullet.being:
					if music:
						fire_sound.play()
					tank_player1.shoot()
			elif key_pressed[pygame.K_i]:
				num=0
				for mine in tank_player1.mines:
					if mine.active:
						num += 1
				tank_player1.fire_mine()
				# tank_player1.display(screen,delay=1)
				print("123")
				for mine in tank_player1.mines:
					if mine.active:
						num -= 1
				map_stage.mineGroup.add(tank_player1.mines)


			elif key_pressed[pygame.K_g]:
				tank_player1.set_brick()
				map_stage.brickGroup.add(tank_player1.brick_obj)
			elif key_pressed[pygame.K_h]:
				tank_player1.set_tree()
				map_stage.treeGroup.add(tank_player1.tree_obj)

			# 玩家二
			# ↑↓←→ -> 上下左右
			# 小键盘0键射击
			if num_player > 1:
				if key_pressed[pygame.K_UP]:
					tanksGroup.remove(tank_player2)
					tank_player2.move_up(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
					tanksGroup.add(tank_player2)
					player2_moving = True
				elif key_pressed[pygame.K_DOWN]:
					tanksGroup.remove(tank_player2)
					tank_player2.move_down(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
					tanksGroup.add(tank_player2)
					player2_moving = True
				elif key_pressed[pygame.K_LEFT]:
					tanksGroup.remove(tank_player2)
					tank_player2.move_left(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
					tanksGroup.add(tank_player2)
					player2_moving = True
				elif key_pressed[pygame.K_RIGHT]:
					tanksGroup.remove(tank_player2)
					tank_player2.move_right(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
					tanksGroup.add(tank_player2)
					player2_moving = True
				elif key_pressed[pygame.K_KP0]:
					if not tank_player2.bullet.being:
						if music:
							fire_sound.play()
						tank_player2.shoot()
				elif key_pressed[pygame.K_3]:
					num = 0
					for mine in tank_player2.mines:
						if mine.active:
							num += 1
					tank_player2.fire_mine()
					# tank_player1.display(screen,delay=1)
					print("123")
					for mine in tank_player2.mines:
						if mine.active:
							num -= 1
					map_stage.mineGroup.add(tank_player2.mines)
				elif key_pressed[pygame.K_2]:
					tank_player2.set_brick()
					map_stage.brickGroup.add(tank_player2.brick_obj)
				elif key_pressed[pygame.K_3]:
					tank_player2.set_tree()
					map_stage.treeGroup.add(tank_player2.tree_obj)

			# 背景
			screen.blit(bar_img, (0, 0))
			screen.blit(bg_img, (0, 50))
			if music:
				screen.blit(open_img, (580, 5))
			else:
				screen.blit(close_img, (580, 5))
			#        进度条长度及颜色
			bar_with = 250 * (enemytanks_dead / enemytanks_all)
			if enemytanks_dead / enemytanks_all < 0.7500001:
				barProgress_red = barProgress_img.subsurface((0, 46), (bar_with, 25))
				screen.blit(barProgress_red, (60, 17))
			else:
				barProgress_green = barProgress_img.subsurface((0, 0), (bar_with, 24))
				screen.blit(barProgress_green, (60, 17))

			screen.blit(play1, p1rect)  # 贴上玩家1
			play1_score = font_bar.render(str(tank_player1.score), True, (255, 255, 255))  # 玩家1得分
			screen.blit(play1_score, p1rect_score)  # 贴上玩家1得分
			play1_life = font_bar.render(str(tank_player1.life), True, (255, 255, 255))  # 玩家2生命
			screen.blit(play1_life, p1rect_life)  # 贴上玩家1生命

			if num_player > 1:
				screen.blit(play2, p2rect)  # 贴上玩家2
				play2_score = font_bar.render(str(tank_player2.score), True, (255, 255, 255))  # 玩家2得分
				screen.blit(play2_score, p2rect_score)  #贴上玩家2得分
				play2_life = font_bar.render(str(tank_player2.life), True, (255, 255, 255))  # 玩家2生命
				screen.blit(play2_life, p2rect_life)  # 贴上玩家2生命
			# 石头墙
			for each in map_stage.brickGroup:
				screen.blit(each.brick, each.rect)
			# 钢墙
			for each in map_stage.ironGroup:
				screen.blit(each.iron, each.rect)
			# 冰
			for each in map_stage.iceGroup:
				screen.blit(each.ice, each.rect)
			# 河流
			for each in map_stage.riverGroup:
				screen.blit(each.river, each.rect)
			# 树
			for each in map_stage.treeGroup:
				screen.blit(each.tree, each.rect)
			time += 1
			if time == 5:
				time = 0
				is_switch_tank = not is_switch_tank

			# 我方坦克
			if tank_player1 in mytanksGroup:
				if is_switch_tank and player1_moving:
					screen.blit(tank_player1.tank_0, (tank_player1.rect.left, tank_player1.rect.top))
					player1_moving = False
				else:
					screen.blit(tank_player1.tank_1, (tank_player1.rect.left, tank_player1.rect.top))
				if tank_player1.protected:
					screen.blit(tank_player1.protected_mask1, (tank_player1.rect.left, tank_player1.rect.top))
			if num_player > 1:
				if tank_player2 in mytanksGroup:
					if is_switch_tank and player2_moving:
						screen.blit(tank_player2.tank_0, (tank_player2.rect.left, tank_player2.rect.top))
						player1_moving = False
					else:
						screen.blit(tank_player2.tank_1, (tank_player2.rect.left, tank_player2.rect.top))
					if tank_player2.protected:
						screen.blit(tank_player1.protected_mask1, (tank_player2.rect.left, tank_player2.rect.top))
			# 敌方坦克
			for each in enemytanksGroup:
				# 出生特效
				if each.born:
					if each.times > 0:
						each.times -= 1
						if each.times <= 10:
							screen.blit(appearances[2], (3+each.x*12*24, 53))
						elif each.times <= 20:
							screen.blit(appearances[1], (3+each.x*12*24, 53))
						elif each.times <= 30:
							screen.blit(appearances[0], (3+each.x*12*24, 53))
						elif each.times <= 40:
							screen.blit(appearances[2], (3+each.x*12*24, 53))
						elif each.times <= 50:
							screen.blit(appearances[1], (3+each.x*12*24, 53))
						elif each.times <= 60:
							screen.blit(appearances[0], (3+each.x*12*24, 53))
						elif each.times <= 70:
							screen.blit(appearances[2], (3+each.x*12*24, 53))
						elif each.times <= 80:
							screen.blit(appearances[1], (3+each.x*12*24, 53))
						elif each.times <= 90:
							screen.blit(appearances[0], (3+each.x*12*24, 53))
					else:
						each.born = False
				else:
					if is_switch_tank:
						screen.blit(each.tank_0, (each.rect.left, each.rect.top))
					else:
						screen.blit(each.tank_1, (each.rect.left, each.rect.top))
					if each.can_move:
						tanksGroup.remove(each)
						each.move(tanksGroup, map_stage.brickGroup, map_stage.ironGroup, myhome)
						tanksGroup.add(each)


			# 我方子弹
			for tank_player in mytanksGroup:
				if tank_player.bullet.being:
					tank_player.bullet.move()
					screen.blit(tank_player.bullet.bullet, tank_player.bullet.rect)
					# 子弹碰撞敌方子弹
					for each in enemybulletsGroup:
						if each.being:
							if pygame.sprite.collide_rect(tank_player.bullet, each):
								tank_player.bullet.being = False
								each.being = False
								screen.blit(boom_imgs[0], each.rect)

								enemybulletsGroup.remove(each)
								tank_player.score +=1
								break
						else:
							enemybulletsGroup.remove(each)
					# 子弹碰撞敌方坦克
					for each in enemytanksGroup:
						if each.being:
							if pygame.sprite.collide_rect(tank_player.bullet, each):
								tank_player.score += 5
								if each.is_red == True:
									myfood = food.Food()
									myfood.generate()
									myfoodsGroup.add(myfood)
									each.is_red = False
								each.blood -= 1
								each.color -= 1
								if each.blood < 0:
									if music:
										bang_sound.play()
									each.being = False
									enemytanksGroup.remove(each)
									enemytanks_now -= 1
									enemytanks_dead +=1
									tanksGroup.remove(each)
								else:
									each.reload()
								tank_player.bullet.being = False
								break
						else:
							enemytanksGroup.remove(each)
							tanksGroup.remove(each)
					# 子弹碰撞石头墙
					if pygame.sprite.spritecollide(tank_player.bullet, map_stage.brickGroup, True, None):
						tank_player.bullet.being = False
					'''
					# 等价方案(更科学点)
					for each in map_stage.brickGroup:
						if pygame.sprite.collide_rect(tank_player.bullet, each):
							tank_player.bullet.being = False
							each.being = False
							map_stage.brickGroup.remove(each)
							break
					'''
					# 子弹碰钢墙
					if tank_player.bullet.stronger:
						if pygame.sprite.spritecollide(tank_player.bullet, map_stage.ironGroup, True, None):
							tank_player.bullet.being = False
					else:
						if pygame.sprite.spritecollide(tank_player.bullet, map_stage.ironGroup, False, None):
							tank_player.bullet.being = False
					'''
					# 等价方案(更科学点)
					for each in map_stage.ironGroup:
						if pygame.sprite.collide_rect(tank_player.bullet, each):
							tank_player.bullet.being = False
							if tank_player.bullet.stronger:
								each.being = False
								map_stage.ironGroup.remove(each)
							break
					'''
					# 子弹碰大本营
					if pygame.sprite.collide_rect(tank_player.bullet, myhome):
						tank_player.bullet.being = False
						myhome.set_dead()
						is_gameover = True
			# 敌方子弹
			for each in enemytanksGroup:
				if each.being:
					if each.can_move and not each.bullet.being:
						enemybulletsGroup.remove(each.bullet)
						each.shoot()
						enemybulletsGroup.add(each.bullet)
					if not each.born:
						if each.bullet.being:
							each.bullet.move()
							screen.blit(each.bullet.bullet, each.bullet.rect)
							# 子弹碰撞我方坦克
							for tank_player in mytanksGroup:
								if pygame.sprite.collide_rect(each.bullet, tank_player):
									if not tank_player.protected:
										if music:
											bang_sound.play()
										tank_player.life -= 1
										if tank_player.life <1:
											play1_life = font_bar.render(str(tank_player1.life), True,
																		 (255, 255, 255))  # 玩家2生命
											screen.blit(play1_life, p1rect_life)  # 贴上玩家2生命
											if num_player > 1:
												play2_life = font_bar.render(str(tank_player2.life), True,
																		 (255, 255, 255))  # 玩家2生命
												screen.blit(play2_life, p2rect_life)  # 贴上玩家2生命
											mytanksGroup.remove(tank_player)
											tanksGroup.remove(tank_player)
											if len(mytanksGroup) < 1:
												is_gameover = True
										else:
											tank_player.reset()
									each.bullet.being = False
									enemybulletsGroup.remove(each.bullet)
									break
							# 子弹碰撞石头墙
							if pygame.sprite.spritecollide(each.bullet, map_stage.brickGroup, True, None):
								each.bullet.being = False
								enemybulletsGroup.remove(each.bullet)
							'''
							# 等价方案(更科学点)
							for one in map_stage.brickGroup:
								if pygame.sprite.collide_rect(each.bullet, one):
									each.bullet.being = False
									one.being = False
									enemybulletsGroup.remove(one)
									break
							'''
							# 子弹碰钢墙
							if each.bullet.stronger:
								if pygame.sprite.spritecollide(each.bullet, map_stage.ironGroup, True, None):
									each.bullet.being = False
							else:
								if pygame.sprite.spritecollide(each.bullet, map_stage.ironGroup, False, None):
									each.bullet.being = False
							'''
							# 等价方案(更科学点)
							for one in map_stage.ironGroup:
								if pygame.sprite.collide_rect(each.bullet, one):
									each.bullet.being = False
									if each.bullet.stronger:
										one.being = False
										map_stage.ironGroup.remove(one)
									break
							'''
							# 子弹碰大本营
							if pygame.sprite.collide_rect(each.bullet, myhome):
								each.bullet.being = False
								myhome.set_dead()
								is_gameover = True
				else:
					enemytanksGroup.remove(each)
					tanksGroup.remove(each)
			# 家
			screen.blit(myhome.home, myhome.rect)
			# 炸弹
			tanksGroup = pygame.sprite.Group()
			# 所有 地雷碰撞(地形,坦克)情况
			all_active_mines = []
			all_active_mines1 = []
			all_active_mines2 = []
			boom_images = []
			for mine in tank_player1.mines:
				all_active_mines1.append(mine)
				all_active_mines.append(mine)
			if num_player > 1:
				for mine in tank_player2.mines:
					all_active_mines2.append(mine)
					all_active_mines.append(mine)

			for mine in all_active_mines:
				if mine.active:
					screen.blit(mine.image_mine, mine.rect)
					enemy_group = None
					if mine.owner == 1:
						enemy_group = enemytanksGroup
					elif mine.owner == 2:
						enemy_group = enemytanksGroup

					collide_enemy_tanks = pygame.sprite.spritecollide(mine, enemy_group, True)
					for enemy_tank in collide_enemy_tanks:
						if mine in all_active_mines1:
							tank_player1.score+=20
						else:
							tank_player2.score+=20
						enemytanks_now -= 1
						enemytanks_dead += 1
						tanksGroup.remove(enemy_tank)
						boom_image = Tank_boom()
						boom_image.rect.center = enemy_tank.rect.center
						boom_images.append(boom_image)
						mine.active = False
				# self.boom_enemy.play()
			# 食物
			for myfood in myfoodsGroup:
				if myfood.being and myfood.time > 0:
					screen.blit(myfood.food, myfood.rect)
					myfood.time -= 1
					for tank_player in mytanksGroup:
						if pygame.sprite.collide_rect(tank_player, myfood):
							tank_player.score += 10
							# 消灭当前所有敌人
							if myfood.kind == 0:
								for _ in enemytanksGroup:
									if music:
										bang_sound.play()
								enemytanksGroup = pygame.sprite.Group()
								enemytanks_total -= enemytanks_now
								enemytanks_dead+=enemytanks_now
								enemytanks_now = 0
							# 敌人静止
							if myfood.kind == 1:
								for each in enemytanksGroup:
									each.can_move = False
							# 子弹增强
							if myfood.kind == 2:
								if music:
									add_sound.play()
								tank_player.bullet.stronger = True
							# 使得大本营的墙变为钢板
							if myfood.kind == 3:
								map_stage.protect_home()
							# 坦克获得一段时间的保护罩
							if myfood.kind == 4:
								if music:
									add_sound.play()
								for tank_player in mytanksGroup:
									tank_player.protected = True
							# 坦克升级
							if myfood.kind == 5:
								if music:
									add_sound.play()
								tank_player.up_level()
							# 坦克生命+1
							if myfood.kind == 6:
								if music:
									add_sound.play()
								tank_player.life += 1
							# 坦克吃到金币加分
							if myfood.kind == 7:
								add_sound.play()
								tank_player.score += 40
							myfood.being = False
							myfoodsGroup.remove(myfood)
							break
				else:
					myfood.being = False
					myfoodsGroup.remove(myfood)
			pygame.display.flip()
			clock.tick(60)
	if not is_gameover:
		show_end_interface(screen, 630, 680, True)
	else:
		show_end_interface(screen, 630, 680, False)



# 结束界面显示
def show_end_interface(screen, width, height, is_win):
	bg_img = pygame.image.load("./images/others/background.png")
	screen.blit(bg_img, (0, 50))
	font = pygame.font.Font('./font/simkai.ttf', width//10)
	if is_win:
		content = font.render(u'恭喜通关！', True, (255, 0, 0))  #添加游戏分数字样
		rect = content.get_rect()
		rect.midtop = (width/2, height/2)
		screen.blit(content, rect)
	else:
		fail_img = pygame.image.load("./images/others/gameover.png")
		rect = fail_img.get_rect()
		rect.midtop = (width/2, height/2)
		screen.blit(fail_img, rect)
	font2 = pygame.font.Font('./font/simkai.ttf', width // 28)
	restart = font2.render(u'按R键重新开始...',True,(255,0,0))
	restartrect = restart.get_rect()
	restartrect.midtop = (width / 1.8, height / 1.5)
	screen.blit(restart, restartrect)
	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_r:
					main()


if __name__ == '__main__':
	main()