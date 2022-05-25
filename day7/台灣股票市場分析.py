# 本益比, 殖利率, 股價淨值比
#  <10    >5%    < 1 (買) > 1 (賣)
import requests
url = 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=csv&date=20220525&selectType=ALL'

data = requests.get(url).text
#print(data)
# 資料整理
# 將有 - 變成 -1
data = data.replace('"-"', '-1')
print(data)
