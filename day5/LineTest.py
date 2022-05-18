import day5.Line as line

if __name__ == '__main__' :
    # 測試文字傳送
    line.lineNotifyText('Helle World')

    # 測試 sticker 傳送
    line.lineNotifySticker(789, 10887)

    # 測試本地端圖片上傳 傳送
    line.lineNotifyLocalImage('f18.jpg')

    # 測試雲端端圖片 傳送
    imageURI = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/A-10_Thunderbolt_II_In-flight-2.jpg/325px-A-10_Thunderbolt_II_In-flight-2.jpg'
    line.lineNotifyWebImage(imageURI)