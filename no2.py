# ******リストに格納******

# リストを宣言
age_array = []

# キーボードから入力
age = input("年齢を入力>>")

# age_arrayの最後に入力した数字を格納
age_array.append(age)

print(age_array)

"""
# 無限ループ ->no3で注意事項
while(True):
    # 年齢を入力
    age = input("年齢>>")
    # もし入力された年齢が999歳ならストップ
    if(int(age) == 999):
        # 無限ループから抜けるコマンド
        exit()
        # おまけ
        # プログラムを終了させるコマンド
        import sys
        sys.exit()
    else:
        # 配列に格納
        age_array.append(int(age))
        # 表示
        print(age_array)
"""
