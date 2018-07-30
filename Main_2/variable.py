# ーーーカラー
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# ーーーマップブロック関連
block_num = 200  # ブロックの数
start_x = 50  # 初期マップの左端
block_w = 20  # ブロックの幅
block_under = 450  # ブロックの下辺y座標

# ーーーキャラクタ関連
# F = 50  # ジャンプ力
penalty = 0  # ジャンプ回数定数
jump_time = 0  # ジャンプの瞬間
# jump_list = [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1000]  # 1:ジャンプをする
jump_list = [0 for i in range(10 + 1)]
jump_index = 0  # ジャンプリストのインデックス

# ーーー障害物関連
enemy_live = 0
enemy_speed = 20
enemy_init_flag = 0
enemy_list_y = [70, 1000, 0, 70, 1000, 0, 70, 1000, 70, 0, 1000]
enemy_num = 0  # 障害物番号

# 速度
move_speed = 15

# その他
score = 0  # スコア

# ーーーよくわからない変数
flag = 0
