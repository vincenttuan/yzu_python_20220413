# 撰寫一個 LineNotify 推播工具
# 推播文字, 內建小圖, 自訂小圖
import requests
token = ""  # 授權碼
lineNotifyURL = "https://notify-api.line.me/api/notify"  # 發送位置

# 推播文字
def lineNotifyText(msg):
    # 建立 HTTP 的標頭(Header)資訊
    # Authorization 授權
    headers = {
                "Authorization": "Bearer " + token,
                "Content-type": "application/x-www-form-urlencoded"
              }
    payload = {'message': msg}
    response = requests.post(lineNotifyURL, headers=headers, params=payload)
    print('回應碼:', response.status_code)


# 推播內建小圖
def lineNotifySticker(stickerPackageId, stickerId):
    pass


# 推播地端自訂小圖
def lineNotifyLocalImage(imageURI):
    pass



