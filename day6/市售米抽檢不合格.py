import json
import requests
# 市售食米抽檢不合格產品 資料位置
url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
# 取得網站原始文字資料
data = requests.get(url).text
# 將文字資料轉換為 json 格式 (相當於 python 的 dict 字典格式)
# 要轉為 json 格式才能分析
data = json.loads(data)
print(data)
print('資料筆數:', len(data))
# 資料整理
print('資料整理')
bad_foods = []  # 存放資料整理的內容
for item in data:
    food = {'品名': item.get('品名'), '不合格原因': item.get('不合格原因')}
    bad_foods.append(food)
print(bad_foods)
bad_foods = tuple(bad_foods)  # 轉為 tuple 的目的是讓分析速度加快

# 資料分析
print('資料分析')
result = []  # 存放資料分析的結果
keyword = input('請輸入關鍵字:')
for food in bad_foods:
    if keyword in food['品名']:
        result.append(food)

print('資料筆數:', len(result))
for row in result:  # 逐筆印出資料
    print(row)

# 資料存檔
if len(result) > 0:
    file_name = '%s.txt' % keyword
    file = open(file_name, 'w', encoding='UTF-8')
    file.write("關鍵字" + keyword + "不合格商品\n")
    for row in result:
        file.write(str(row))  # 將 row 轉為字串格式
        file.write("\n")
    print('%s.txt 存檔成功' % keyword)
else:
    print('關鍵字 %s 沒有資料' % keyword)
