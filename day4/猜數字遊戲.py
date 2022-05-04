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
ans = 38
min = 0
max = 100
while True:
    user_guess = int(input('使用者 %d ~ %d 之間猜一數字: ' % (min, max)))
    # 判斷是否有猜對 ?
    if user_guess < ans:
        min = user_guess
    elif user_guess > ans:
        max = user_guess
    else:
        print('恭喜答對')
        break

