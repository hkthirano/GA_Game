import pygame

from variable import *


class Block():
    def __init__(self):
        # マップブロックの初期化
        self.map_arr = [[0 for i2 in range(2)] for i1 in range(block_num)]
        #map_arr_y = [0 for i in range(block_num)]
        map_arr_y = [300 for i in range(block_num)]

        '''
        # マップデータを読み込む
        tmp_data = open('map.txt', 'r')
        for (i, data) in zip(range(block_num), tmp_data):
            map_arr_y[i] = int(data)
        '''

        # マップブロックの座標を格納
        tmp_x = start_x
        for (map_arr_data, y) in zip(self.map_arr, map_arr_y):
            map_arr_data[0] = tmp_x + block_w
            map_arr_data[1] = y
            tmp_x = map_arr_data[0]

    def move(self, speed):
        for i in range(block_num):
            self.map_arr[i][0] -= speed

    def draw_map(self, screen):
        for (i, map_arr_data) in zip(range(block_num), self.map_arr):
            block_h = block_under - map_arr_data[1]
            block = (map_arr_data[0], map_arr_data[1], block_w, block_h)
            # ブロック50個ごとに目印
            if i % 50 == 0:
                pygame.draw.rect(screen, BLACK, block)
            # ゴールの目印
            elif i == block_num - 1:
                pygame.draw.rect(screen, YELLOW, block)
            else:
                pygame.draw.rect(screen, RED, block)
