scores = [89, 95, 90, 83, 43, 62, 57]
# 請用 for 迴圈試算總分, 平均
if __name__ == '__main__':
    print(scores)
    sum = 0
    for score in scores:  # 依序取得每一筆分數
        #print(score) #印出每一筆分數
        sum = sum + score  # 每一筆分數與 sum 進行累加
    print('總分:', sum)
    print('平均:', sum/len(scores))