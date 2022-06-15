import cv2

# 設定攝像鏡頭(0, 1, 2, ...)
cap = cv2.VideoCapture(0)

# 判斷 camera 是否有啟動 ?
if not cap.isOpened():
    cap.open()  # 啟動

print(cap.isOpened())
# 設定捕捉區域
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while True:
    # 捕捉 frame
    ret, frame = cap.read()
    print(frame)

# 釋放資源
cap.release()
cv2.destroyAllWindows()
