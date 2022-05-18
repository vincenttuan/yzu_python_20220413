'''
Python 數組
list = [1, 3, 5, 7, 5] 內容可重複/可變更
tuple = (1, 3, 5, 7, 5) 內容可重複/不可變更
set = (1, 3, 5, 7) 內容不可重複
dict = {'name': 'John', 'age': 18} key:value 元素集合
'''
# list
x = [1, 3, 5, 7, 5]
print(x, type(x))
x.append(9)
print(x)
x = tuple(x)  # list 轉 tuple
print(x, type(x))
# x.append(11) # tuple 數組不可以增加元素
x = list(x)  # tuple 轉 list


