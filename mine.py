import pygame
# 地雷

import time as t

import time, subprocess

def stopWatch(m, s):
    timeLeft = 60*m + s
    while timeLeft > 0:
        print(timeLeft, end='')
        time.sleep(1)
        timeLeft -= 1

    #倒计时结束，播放提示音乐。
    # subprocess.Popen(['start', 'alarm.mp3'], shell=True)


class Mine(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load_image()
        self.rect = self.image_mine.get_rect()
        # 1 为我方阵营, 2 为敌方阵营
        self.owner = 1
        # 此刻是否处于被激活状态, 若是,则绘制子弹
        self.active = False

    def load_image(self):
        self.image_mine = pygame.image.load("./images/others/mine.png").convert_alpha()