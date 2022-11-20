import cv2


fourcc = cv2.VideoWriter_fourcc('D','I','V','X')

# 创建输出文件
vw = cv2.VideoWriter("/Users/xkzhai/OpenCV_Python/video/out.avi",fourcc,25,(1280,720)) 
# 创建窗口
cv2.namedWindow('video',cv2.WINDOW_NORMAL)
cv2.resizeWindow('video',640 ,360)

# 获取视频设备
cap = cv2.VideoCapture(0)
 
 
while cap.isOpened(): # 判断摄像头是否打开
    # 从摄像头读取视频帧
    ret, frame = cap.read()

    if ret == True: 
        # 将视频帧在窗口显示
        cv2.imshow('video',frame)
        cv2.resizeWindow('video',640 ,360) # 重新将窗口设置为指定大小

        # 写数据到文件
        vw.write(frame)

        # 等待键盘事件,如果为q，退出
        key = cv2.waitKey(1)
        
        
        if(key & 0xFF == ord('q')):
            break
    else:
        break
# 释放VideoCapture
cap.release()
vw.release()
cv2.destroyAllWindows()