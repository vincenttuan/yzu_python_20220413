# 處理數字的涵式集
# 小數點 n 位 + 千分號
# n=1 小數點 n 位 預設值是 1
# mark=True 表示是否要加上千分號
def get(num, n=1, mark=True):
    num = int(num * 10**n)/10**n
    if mark: # if mark == True
        result = format(num, ",")
    else:
        result = num
    return result

# 處理股價的交易成本
# price 股票價格
# shares 股票股數 (=1000)
# rate 手續費率 (=0.001425)
def getBuyCost(price, shares=1000, rate=0.001425):
    cost = price * shares
    cost = cost + (cost * rate)
    return cost


