# 迴圈 for-loop 步進迴圈
# 印出 1~9 的數字
for i in range(1, 10):
    print(i, end=', ')

print()

for i in range(1, 10, 3):
    print(i, end=', ')

print()

# 數組(陣列)符號 : [ ]
scores = [100, 40, 80, 35, 75]
# index   0    1   2   3   4
for score in scores:
    if score >= 60:
        print(score, end=', ')

print()
print(scores[0])  # 抓取 index = 0 的資料
print(scores[1])  # 抓取 index = 1 的資料



