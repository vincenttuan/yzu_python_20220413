poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
#位置     0    1    2    3    4    5    6    7    8    8     10   11   12
#洗牌前
print(poker)
#洗牌
p1 = 3
p2 = 5
num = poker[p1]
poker[p1] = poker[p2]
poker[p2] = num
#洗牌後
print(poker)
