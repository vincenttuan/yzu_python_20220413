# 迴圈 while
import random as r
print('進入迴圈')
while True:
    n = r.randint(1, 99) # 取 1~99 的隨機數
    print(n)
    if n == 99:
        break  # 強制離開迴圈

print('離開迴圈')