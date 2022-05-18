# 將 salary.txt 的檔案資料內容讀取出來
file = open('salary.txt', 'r', encoding='UTF-8')
# 一次讀取所有資料
alldata = file.read()
file.close()
print(alldata)
