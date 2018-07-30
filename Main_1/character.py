import pygame
import math

from variable import *


class Character():
    def __init__(self):
        # キャラクタの初期位置
        self.x = 150
        self.y = 270 - 1
        self.y_init = 270 - 1
        self.y_prev = 0
        self.flay = 0
        self.F = 50
        self.F_init = 50

    def jump(self):
        self.flay = 1
        self.y -= self.F
        self.F = -5

    def move(self):
        self.y -= (self.y_prev - self.y) + self.F
        if self.y_init - self.y < 3:
            self.flay = 0
            self.F = self.F_init

    def draw_chara(self, screen):
        # 大きさ30x30のキャラクタ
        rect = pygame.Rect(self.x, self.y, 30, 30)
        pygame.draw.rect(screen, BLACK, rect)

    def check_hit(self, enemy):
        chara_center = [self.x + 15, self.y + 15]
        enemy_center = [enemy.x + 10, enemy.y + 10]

        r = pow((chara_center[0]-enemy_center[0]), 2) + \
            pow((chara_center[1] - enemy_center[1]), 2)

        r = math.sqrt(r)

        if r < 25:
            return 1
