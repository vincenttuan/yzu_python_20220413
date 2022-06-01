# 例外處理
# 取得使用者所輸入的整數數值
def input_int():
    try:
        y = int(input('請輸入分母: '))
    except ValueError as e:
        print('請輸入數字, 錯誤內容:', e)
    else:
        return y

# 計算除法
def div(y):
    x = 100
    try:
        result = x / y  # ZeroDivisionError 分母不可為 0
    except ZeroDivisionError as e:
        print('分母不可為 0, 錯誤內容:', e)
    else:
        return x, y, result

# 印出結果
def print_result(x, y, result):
    print('%d / %d = %.1f' % (x, y, result))

# 組合
def div_process():
    try:
        y = input_int()
        x, y, result = div(y)
    except:
        div_process()
    else:
        print_result(x, y, result)

def div_process2():
    try:
        y = input_int()
        y = y * 2
        x, y, result = div(y)
    except:
        div_process()
    else:
        print_result(x, y, result)

if __name__ == '__main__':
    div_process2()