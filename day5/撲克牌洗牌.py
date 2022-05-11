poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#位置     0    1    2    3    4    5    6    7    8    8     10   11   12
#洗牌前
print(poker)
#洗牌
num = poker[0]  # 將 poker[0] 的資料給 num
poker[0] = poker[1]  # 將 poker[1] 的資料給 poker[0]
poker[1] = num  # 將 num 的資料給 poker[1]
#洗牌後
print(poker)
