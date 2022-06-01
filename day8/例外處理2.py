# 例外處理
# 計算除法
def div():
    x = 100
    try:
        y = int(input('請輸入分母: '))  # ValueError
        result = x / y  # ZeroDivisionError 分母不可為 0
    except ValueError as e:
        print('請輸入數字, 錯誤內容:', e)
        div()
    except ZeroDivisionError as e:
        print('分母不可為 0, 錯誤內容:', e)
        div()
    else:
        print('%d / %d = %.1f' % (x, y, result))

if __name__ == '__main__':
    div()