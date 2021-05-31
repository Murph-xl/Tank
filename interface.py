from tkinter import *

import pygame
from pygame import FULLSCREEN, QUIT
# 开始界面显示
def show_start_interface(screen, width, height):

    bg_img = pygame.image.load("./images/others/bg_start.png")
    screen.blit(bg_img, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 1
                if event.key == pygame.K_2:
                    return 2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    sys.exit() # 退出系统

# 皮肤选择
def show_select_interface(screen,width,heigth,player):
    pygame.display.set_caption("选择皮肤")
    #加载字体
    font1 = pygame.font.Font('font/STHeiti-Light-3.ttc', 630 // 20)
    font2 = pygame.font.Font('font/STHeiti-Light-3.ttc', 630 // 20)
    #加载背景
    bg_img = pygame.image.load("images/renwubg .png")
    #加载选择框
    kuang_img = pygame.image.load("images/kuang.png")
    #加载坦克
    img_one = pygame.image.load("images/tank0.png")
    img_two = pygame.image.load("images/tank1.png")
    img_three = pygame.image.load("images/tank2.png")
    img_four = pygame.image.load("images/tank3.png")
    img_five = pygame.image.load("images/tank4.png")

    #定义初始x：67，移动步长：100
    nowX = 67
    step = 100

    #文本内容
    selectText = font1.render(u"选择人物", True, (149, 221, 232))
    myText_rect = selectText.get_rect()
    myText_rect.midtop = (320, 150)
    playerText = font2.render(u"player " + str(player), True, (246, 242, 244))
    playerText_rect = playerText.get_rect()
    playerText_rect.midtop = (320, 580)

    while True:
        screen.blit(bg_img, (0, 0))
        screen.blit(selectText, myText_rect)  #
        screen.blit(playerText, playerText_rect)  #
        screen.blit(img_one, (55, 310))
        screen.blit(img_two, (155, 310))
        screen.blit(img_three, (255, 310))
        screen.blit(img_four, (355, 310))
        screen.blit(img_five, (455, 310))
        screen.blit(kuang_img, (nowX, 321))
        # 获取事件
        for event in pygame.event.get():
            # 判断事件是否为退出事件
            if event.type == QUIT:
                # 退出pygame
                pygame.quit()
                sys.exit() # 退出系统
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    sys.exit() # 退出系统
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if nowX < 455:
                        nowX += step
                    screen.blit(kuang_img, (nowX, 321))
                    pygame.display.update()
                if event.key == pygame.K_LEFT:
                    if nowX > 155:
                        nowX -= step
                    screen.blit(kuang_img, (nowX, 321))
                    pygame.display.update()
                if event.key == pygame.K_SPACE:
                    return int(nowX / step)

        pygame.display.update()


# 关卡切换
def show_switch_stage(screen, width, height, stage):
    if stage == 1:
        bg_img = pygame.image.load("./images/others/level1.png")
    elif stage ==2:
        bg_img = pygame.image.load("./images/others/level2.png")
    elif stage == 3:
        bg_img = pygame.image.load("./images/others/level3.png")
    elif stage ==4:
        bg_img = pygame.image.load("./images/others/level4.png")
    elif stage == 5:
        bg_img = pygame.image.load("./images/others/level5.png")
    else:
        bg_img = pygame.image.load("./images/others/level6.png")
    screen.blit(bg_img, (0, 0))
    pygame.display.update()
    delay_event = pygame.constants.USEREVENT
    pygame.time.set_timer(delay_event, 1000)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                    sys.exit()
            elif event.type == delay_event:
                return
