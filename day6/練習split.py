import re
# 練習 split
# 將字串分割成數組
#      姓名  年齡 身高  體重
str = "John,18# 170; 60"
print(str)
datas = re.split('#|,|;', str)
print(datas, type(datas))

print(datas[0].strip())  # 姓名
print(datas[1].strip())  # 年齡
print(datas[2].strip())  # 身高
print(datas[3].strip())  # 體重
h = int(datas[2])
w = int(datas[3])
bmi = w / (h/100)**2
print(bmi)

