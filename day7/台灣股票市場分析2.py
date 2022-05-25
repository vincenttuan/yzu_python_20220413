import requests

from day7.OO6 import Stock

# 取得所有股票資料
def get_stock_list():
    url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=20220525&selectType=ALL'
    data = requests.get(url).text
    data = data.replace('"-"', '-1')
    data = data.replace('"', '')
    # stock_list 數組集合(存放所有 Stock 物件的地方)
    stock_list = []
    for row in data.split('\r\n'):
        val = row.split(",")
        if len(val) == 8 and val[0] != '證券代號':
            name = val[0]  # 股票名稱
            pe = float(val(4))  # 本益比
            rate = float(val(2))  # 殖利率
            pb = float(val(5))  # 股價淨值比
            # 建立 Stock 物件
            stock = Stock(name, pe, rate, pb)
            # 將 Stock 物件統一裝進 stock_list 數組集合中
            stock_list.append(stock)

    return stock_list

