# 資料轉型
# 字串轉數字: int(字串變數)
# 字串轉浮點數: float(字串變數)
# 整數轉浮點數: float(整數變數)
# 數字轉字串: str(數字變數)
chinese = '90'  # 國文考 90 分
english = '85'  # 英文考 80 分
math = 70  # 數學考 70 分
# 請求出平均 = ?
chinese = int(chinese)  # 將 chinese 字串內容轉 int
print(type(chinese))
english = int(english)
print(type(english))
sum = chinese + english + math
print('總分:' + str(sum))
print('平均:' + str(sum/3))
print('平均:' + str(sum//3))  # 取到整數

