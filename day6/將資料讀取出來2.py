# 將 salary.txt 的檔案資料內容讀取出來
file = open('salary.txt', 'r', encoding='UTF-8')
# 將資料讀入數組 list 中
list = file.readlines()
file.close()
print(list)
sum = 0
for item in list:
    item = item.strip('\n')  # 去除 strip
    #print(item)
    item = item.split(", ")  # split 分割資料
    #print(item)
    salary = int(item[1])
    print(salary, type(salary))
    sum = sum + salary
print('總薪資:', sum)