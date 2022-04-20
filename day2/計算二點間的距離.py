# 計算二點間的距離
# A(x1, y1) B(x2, y2)
# A(10, 20) B(55, 120)
import math

x1, y1 = 10, 20
x2, y2 = 55, 120
dx = math.pow(x1 - x2, 2)  # 相當於 (x1-x2)**2
dy = math.pow(y1 - y2, 2)
d = math.sqrt(dx + dy)
print('距離:', d)
