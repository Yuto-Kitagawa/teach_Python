# リストのコピー

# リストを宣言
array = [1, 2, 3, 4, 5]

j = array
copy = array.copy()

# 配列の0番目を6に変更
array[0] = 6

print(j)  # [6,2,3,4,5]
print(copy)  # [1,2,3,4,5]
