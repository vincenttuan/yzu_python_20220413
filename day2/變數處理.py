# python 保留字
import keyword
print(keyword.kwlist)  # 印出python 保留字

# 變數的連續覆值
a = b = c = 100
print(a, b, c)  # 印出 a, b, c 的值
print(type(a), type(b), type(c))  # 印出 a, b, c 的型態

name, age = 'John', 18
print(name, age)
print(type(name), type(age))

print(age * 2)
print(name * 2)
print(name * age)
print(age + age)
print(name + name)
# print(name + age)  # 執行錯誤
print(name + str(age))  # 將 age 的執行當下轉成 string

# 浮點數
r = 3.14
v = 3.14e2  # 科學記號(浮點數)
print(r, v)
print(type(r), type(v))

# 綜合練習
a, b, c, d = 10, 20.5, True, 'Mary'
print(a, b, c, d)
print(type(a), type(b), type(c), type(d))
# 讓如何讓 a, b, c, d 四個變數 "+"
#print(a + b + c + d) # 錯誤
print(str(a) + str(b) + str(c) + str(d))
print(str(a + b) + str(c) + str(d))

# del 刪除變數
score = 100
print('分數:', score)
print('分數:' + str(score))
del score
#print(score) 產生 NameError: name 'score' is not defined

