# 使用者輸入身高與體重
import math
# shorturl.at/dgiI5

h = float(input('請輸入身高(cm):'))
w = float(input('請輸入體重(kg):'))
h = h / 100  # cm -> m
bmi = w / h**2
print(bmi)
bmi = w / math.pow(h, 2)
print(bmi)

