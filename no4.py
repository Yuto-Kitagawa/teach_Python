# ******文字の切り取り(スライス)******
array = [0, 1, 2, 3, 4, 5, 6]

# 未満
print(array[0:4])
# 以上
print(array[4:len(array)])

print("あいうえおかきくけこ"[:4])

"""
string = "まじか、明日雨か。"
# 句読点ありの文字数
print(len(str(string)))

# 句読点なしの文字数
counter = 0
for i in range(len(string)):
    if(string[i] == "、" or string[i] == "。"):
        pass
    else:
        counter += 1
print(counter)

"""
