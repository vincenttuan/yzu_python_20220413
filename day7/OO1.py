# 物件導向
# 建立一個 Human 的類別
class Human:
    name = ''  # 屬性/欄位/變數
    age = 0
    sex = ''

if __name__ == '__main__':
    # 建立一個物件
    h1 = Human()
    h1.name = 'Vincent';h1.age = 18;h1.sex='男'
    # 再建立一個物件
    h2 = Human()
    h2.name = 'Anita';h2.age = 19;h2.sex = '女'

    print(h1)