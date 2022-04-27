# 處理數字的涵式集
# 小數點 n 位 + 千分號
def get(num, n):
    num = int(num * 10**n)/10**n
    result = format(num, ",")
    return result
