str = 'she sell sea shell on the sea shore'
print(str)
print('有幾個字?', len(str))
print('有幾個單字?', len(str.split(' ')))
print('2~10範圍的字串內容', str[2:11])
print('有幾個 s ?', str.count('s'))
print('最近的 sea 在哪一個位置 ?', str.find('sea'))
print('最近的 tea 在哪一個位置 ?', str.find('tea'))
str = '   母親節 快樂 !         '
print(str)
#str = str.lstrip() # 去除左側空白
#str = str.rstrip() # 去除右側空白
str = str.strip() # 去除左右空白
print(str)
