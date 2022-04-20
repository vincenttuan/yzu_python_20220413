# 股票代號 2330.TW
# 股票名稱 台積電
# 目前市價 550.5
# 買進價格 530
# 買進股數 6000
# 手續費 0.001425 (買賣都要算)
# 交易稅 0.003 (賣出要算)
# 如何計算投資金額與獲利狀態
symbol = '2330.TW'
name = '台積電'
price = 550.5
cost = 530
shares = 6000
fee = 0.001425
tax = 0.003
# 請問買入成本 = ?
buy_cost = shares * cost
fee_cost = buy_cost * fee
buy_cost_total = buy_cost + fee_cost
print("股票:%s 買入股數:%d 買入成本:%.1f" % (name, shares, buy_cost_total))
print("股票:%s 買入股數:%s 買入成本:%s" % (name, format(shares, ','), format(buy_cost_total, ',')))

