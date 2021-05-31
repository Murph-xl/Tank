from tkinter import *

import pygame
from pygame import FULLSCREEN, QUIT


# 开始界面显示
def show_start_interface(screen, width, height):
    tfont = pygame.font.Font('./font/simkai.ttf', width // 4)
    cfont = pygame.font.Font('./font/simkai.ttf', width // 20)
    cfont1 = pygame.font.Font('./font/simkai.ttf', width // 30)
    title = tfont.render(u'坦克大战', True, (255, 0, 0))
    content1 = cfont.render(u'按1键进入单人游戏', True, (255, 255, 255))
    content2 = cfont.render(u'按2键进入双人人游戏', True, (255, 255, 255))
    content3 = cfont1.render(u'玩家1：WASD、空格射击   ESC退出', True, (0, 255, 255))
    content4 = cfont1.render(u'玩家2：↑←↓→、小键盘0射击  Q退出', True, (0, 255, 255))

    trect = title.get_rect()
    trect.midtop = (width / 2, height / 4)
    crect1 = content1.get_rect()
    crect1.midtop = (width / 2, height / 1.8)
    crect2 = content2.get_rect()
    crect2.midtop = (width / 2, height / 1.6)
    crect3 = content3.get_rect()
    crect3.midtop = (width / 2, height / 1.4)
    crect4 = content4.get_rect()
    crect4.midtop = (width / 2, height / 1.3)
    screen.blit(title, trect)
    screen.blit(content1, crect1)
    screen.blit(content2, crect2)
    screen.blit(content3, crect3)
    screen.blit(content4, crect4)

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


# 皮肤选择
def show_select_interface(screen, width, heigth, player):
    pygame.display.set_caption("选择皮肤")
    # 加载字体
    font1 = pygame.font.Font('font/STHeiti-Light-3.ttc', 630 // 20)
    font2 = pygame.font.Font('font/STHeiti-Light-3.ttc', 630 // 20)
    # 加载背景
    bg_img = pygame.image.load("images/renwubg .png")
    # 加载选择框
    kuang_img = pygame.image.load("images/kuang.png")
    # 加载坦克
    img_one = pygame.image.load("images/tank0.png")
    img_two = pygame.image.load("images/tank1.png")
    img_three = pygame.image.load("images/tank2.png")
    img_four = pygame.image.load("images/tank3.png")
    img_five = pygame.image.load("images/tank4.png")

    # 定义初始x：67，移动步长：100
    nowX = 67
    step = 100

    # 文本内容
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
                # 退出系统
                sys.exit()
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
    bg_img = pygame.image.load("./images/others/background.png")
    screen.blit(bg_img, (0, 0))
    screen.blit(bg_img, (0, 50))
    font = pygame.font.Font('./font/simkai.ttf', width // 10)
    content = font.render(u'第%d关' % stage, True, (0, 255, 0))
    rect = content.get_rect()
    rect.midtop = (width / 2, height / 2)
    screen.blit(content, rect)
    pygame.display.update()
    delay_event = pygame.constants.USEREVENT
    pygame.time.set_timer(delay_event, 1000)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == delay_event:
                return
