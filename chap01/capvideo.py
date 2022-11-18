import cv2

# 创建窗口
cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640,480)

# 获取视频设备
# cap = cv2.VideoCapture(0)

# 获取视频文件，从视频文件中读取视频帧
cap = cv2.VideoCapture("/Users/xkzhai/OpenCV_Python/video/Beer.mp4")

while True:
    # 从摄像头读取视频帧
    ret, frame = cap.read()

    # 将视频帧在窗口显示
    cv2.imshow('video',frame)

    # 等待键盘事件,如果为q，退出
    # key = cv2.waitKey(1)
    
    # 需与视频文件的帧数一致
    key = cv2.waitKey(40)
    
    if(key & 0xFF == ord('q')):
        break

# 释放VideoCapture
cap.release()
cv2.destroyAllWindows()