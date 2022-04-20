# 使用者輸入: input('提示內容') 會得到字串
import math  # 載入數學工具資源

r = float(input('請輸入半徑:'))
#r = float(r)
print(r, type(r))
#area = r**2 * math.pi
area = math.pow(r, 2) * math.pi
print('面積:', area)
