# 例外處理
x = 100
# 使用者輸入分母
try:
    y = int(input('請輸入分母: '))  # ValueError 使用者輸入不是 int
    result = x / y  # ZeroDivisionError 分母不可為 0
    #print('%d / %d = %.1f' % (x, y, result))
except ValueError as e:
    print('請入數字, 錯誤內容:', e)
except ZeroDivisionError as e:
    print('分母不可為 0, 錯誤內容:', e)
else:
    print('%d / %d = %.1f' % (x, y, result))

