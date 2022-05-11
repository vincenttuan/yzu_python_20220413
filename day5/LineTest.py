import day5.Line as line

if __name__ == '__main__' :
    # 測試文字傳送
    line.lineNotifyText('Helle World')

    # 測試 sticker 傳送
    line.lineNotifySticker(789, 10887)

    # 測試本地端圖片上傳 傳送
    line.lineNotifyLocalImage('f16.jpg')

