import pygame
import math

from variable import *
import block
import character as ch
import enemy
import quit_game as q_g

# ーーー初期設定
pygame.init()
screen = pygame.display.set_mode((640, 480))
myclock = pygame.time.Clock()
font = pygame.font.Font(None, 55)  # フォントの設定(30px)
# screen.fill(((255, 255, 255)))

# ーーーマップブロックの初期化
map_block = block.Block()

# ーーーキャラクタの初期化
main_chara = ch.Character()

# ーーーゲーム実行
while flag == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = 1
    screen.fill(WHITE)
    # ーーー

    # ーーーブロック関連
    # ブロックの移動
    map_block.move(move_speed)
    # ブロックの描画
    map_block.draw_map(screen)

    # ーーーキャラクタ関連
    main_chara.y_prev = main_chara.y
    # ジャンプ
    press = pygame.key.get_pressed()
    if press[pygame.K_UP] and (main_chara.flay == 0):
        penalty += 1
        main_chara.jump()

    if main_chara.flay == 1:
        main_chara.move()

    # キャラクタ描画
    main_chara.draw_chara(screen)

    # ーーー障害物関連
    # 障害物があるかどうか
    if enemy_live == 0:
        enemy_live = 1

    if enemy_live == 1:
        # ー障害物の初期化
        if enemy_init_flag == 0:
            enemy_init_flag = 1
            main_enemy = enemy.Enemy()
        main_enemy.move(enemy_speed)
        main_enemy.draw_map(screen)
        # あたり判定
        if main_chara.check_hit(main_enemy):
            q_g.quit_game(score, penalty)

    # 障害物の削除
    if main_enemy.x < (main_chara.x-50):
        main_enemy = None
        enemy_live = 0
        enemy_init_flag = 0

    # ーーーゴール判定
    if main_chara.x > map_block.map_arr[block_num - 1][0]:
        q_g.quit_game(score, penalty)

    # ーーースコア表示
    score += 1
    # 描画する文字列の設定
    text = font.render('Score:' + str(score), True, BLACK)
    text2 = font.render('Jump:'+str(penalty), True, BLACK)
    # 文字列の表示位置
    screen.blit(text, [20, 20])
    screen.blit(text2, [20, 60])

    # ーーー
    pygame.display.flip()
    myclock.tick(60)
    pygame.display.update()

pygame.quit()
