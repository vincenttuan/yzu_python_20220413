'''
Python 數組
list = [1, 3, 5, 7, 5] 內容可重複/可變更
tuple = (1, 3, 5, 7, 5) 內容可重複/不可變更
set = {1, 3, 5, 7} 內容不可重複
dict = {'name': 'John', 'age': 18} key:value 元素集合
'''
# list
x = [1, 3, 5, 7, 5]
print(x, type(x))
x.append(9)
print(x)

# tuple
x = tuple(x)  # list 轉 tuple
print(x, type(x))
# x.append(11) # tuple 數組不可以增加元素
x = list(x)  # tuple 轉 list

# set
s = set()
s.add(1);s.add(2);s.add(1)
print(s, type(s))

# dict (字典格式, key: value)
e1 = {'name': 'John', 'salary': 50000}
e2 = {'name': 'Mary', 'salary': 40000}
e3 = {'name': 'July', 'salary': 70000}
# 將 e1, e2, e3 三個字典放到 list 數組中
emps = [e1, e2, e3]
print(emps)
# 列出每一筆元素資料
for emp in emps:
    print(emp, emp['name'], emp['salary'])
