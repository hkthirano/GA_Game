import pygame
import random

from variable import *


class Enemy():
    def __init__(self):
        # ーーー障害物は１画面に１つ
        # 障害物があるかどうか
        self.x = 600

        self.y = 270 - random.choice(enemy_random_y)
        self.w = 20
        self.h = 20
        #self.info = (self.x, self.y, self.w, self.h)

    def move(self, speed):
        self.x -= speed

    def draw_map(self, screen):
        info = (self.x, self.y, self.w, self.h)
        pygame.draw.rect(screen, BLUE, info)
