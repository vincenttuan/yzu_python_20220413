'''
min  max
0  ~ 100 之間猜一個數字
--------------------
20 ~ 100
20 ~ 65
30 ~ 65
30 ~ 47
30 ~ 41
36 ~ 41
38
'''
import random as r
min = 0
max = 100
#ans = r.randint(1, 99)
ans = r.randint(min+1, max-1)
while True:
    # user 猜數字
    user_guess = int(input('使用者 %d ~ %d 之間猜一數字: ' % (min, max)))
    # 判斷 user 所猜的是否是合法的資料範圍 ?
    if user_guess <= min or user_guess >= max:
        print('數字範圍錯誤')
        continue  # 重跑回圈

    # 判斷 user 是否有猜對 ?
    if user_guess < ans:
        min = user_guess
    elif user_guess > ans:
        max = user_guess
    else:
        print('恭喜 user 答對')
        break
    #-------------------------------------------------------------------
    # pc 猜數字
    # min  max    min+1   max-1
    # 20 ~ 65 ==> 21   ~  64
    pc_guess = r.randint(min+1, max-1)
    print('pc 猜:', pc_guess)
    if pc_guess < ans:
        min = pc_guess
    elif pc_guess > ans:
        max = pc_guess
    else:
        print('恭喜 pc 答對')
        break


