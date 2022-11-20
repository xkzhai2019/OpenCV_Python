import cv2
# 创建窗口
cv2.namedWindow('trackbar')

import numpy as np

def callback():
    pass
# 创建trackBar
cv2.createTrackbar('R','trackbar' ,0,255,callback)
cv2.createTrackbar('G','trackbar' ,0,255,callback)
cv2.createTrackbar('B','trackbar' ,0,255,callback)

# 创建背景图片
img = np.zeros((480,640,3),np.uint8)

while True:
    # 获取当前trackbar值
    r = cv2.getTrackbarPos('R','trackbar')
    g = cv2.getTrackbarPos('G','trackbar')
    b = cv2.getTrackbarPos('B','trackbar')

    # 改变背景图片
    img[:] = [b,g,r]
    cv2.imshow('trackbar',img)

    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
