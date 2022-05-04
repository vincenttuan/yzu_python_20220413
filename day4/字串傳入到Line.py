# 如何透過 LineNotify 將程式所輸出的字串在 Line 中顯示
# 類似聊天機器人
import requests
token = 'l7dMZUhjw5vlqt3KhGdUA4kpjzlqIeHKCwWB0kW40xL'

# 用來通知 Line
def lineNotifyMessage(msg):
    # 建立 HTTP 的標頭(Header)資訊
    # Authorization 授權
    headers = {
                "Authorization": "Bearer " + token,
                "Content-type": "application/x-www-form-urlencoded"
              }
    payload = {'message': msg}
    response = requests.post("https://notify-api.line.me/api/notify",
                         headers=headers, params=payload)
    print('回應碼:', response.status_code)

# 主程式
if __name__ == '__main__':
    msg = '\n母親節\n快樂 ! YA~~'
    lineNotifyMessage(msg)



