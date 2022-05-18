import json
import requests
# 市售食米抽檢不合格產品 資料位置
url = 'https://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'
# 取得網站原始文字資料
data = requests.get(url).text
# 將文字資料轉換為 json 格式 (相當於 python 的 dict 字典格式)
# 要轉為 json 格式才能分析
data = json.loads(data);
print(data)


