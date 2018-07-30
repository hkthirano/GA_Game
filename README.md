# GA_Game

遺伝的アルゴリズムでゲームを学習させます。

ゲームはジャンプして障害物を交わすだけです。

記事をQittaに載せてます。

[遺伝的アルゴリズム(Python)でマリオをクリアしたかったのに・・・]()

![result](https://github.com/hokuto-HIRANO/GA_Game/blob/master/movie/output.gif)

---

## Main_1 : お試し用

+ 実行
```
cd Main_1
python main.py
```
+ ↑でジャンプ

---

## Main_2 : 学習用

+ 実行
```
cd Main_2
python main.py * * * * * * * * * *
# 引数に遺伝子10個を与える
# ex. python main.py 0 0 1 0 0 1 0 0 0 1
# 1:ジャンプする 0:ジャンプしない
```

---

## GA : Main_2を使って遺伝的アルゴリズムで学習させる

+ 実行
```
cd GA
python main.py
```