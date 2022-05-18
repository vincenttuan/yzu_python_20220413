file = open('salary.txt', 'w', encoding='UTF-8')
# 寫入 John 50000
file.write("John, 50000\n")  # 資料寫入到檔案
file.write("Mary, 40000\n")
file.write("July, 70000\n")
file.close()  # 關閉檔案
print("寫檔完成")
