import cv2

# 定義臉部偵測特徵檔
face_cascade = cv2.CascadeClassifier('./xml/haarcascade_frontalface_alt.xml')

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
    #print(frame)

    # 偵測人臉
    faces = face_cascade.detectMultiScale(
        frame, # 待檢測圖片
        scaleFactor=1.1,  # 檢測粒度
        minNeighbors=5,  # 每個目標至少要檢測幾次以上才認定
        minSize=(30, 30),  # 搜尋最小尺寸
        flags=cv2.CASCADE_SCALE_IMAGE  # 正常比例檢測
    )

    amount = len(faces)
    if(amount > 0):
        print('找到 %d 個人臉' % amount)

    # 將 frame 資料顯示
    cv2.imshow('My camera', frame)

    # 按下 q 離該
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

# 釋放資源
cap.release()
cv2.destroyAllWindows()
