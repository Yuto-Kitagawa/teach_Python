# おみくじのプログラム

import random

# ランダムな数字を生成
randamu = random.randint(0, 4)

if(randamu == 0):
    print("大吉！とても運がいい！")

if(randamu == 1):
    print("中吉！まぁまぁだね！")

if(randamu == 2):
    print("小吉！ビミョー。頑張れえよ！")

if(randamu == 3):
    print("凶！ちょっとあかんな―")

if(randamu == 4):
    print("大凶！最悪！！")
