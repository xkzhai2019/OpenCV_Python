import cv2

cv2.namedWindow("img",cv2.WINDOW_NORMAL)

img = cv2.imread("/Users/xkzhai/OpenCV_Python/img/lena.jpg")

while True:

    cv2.imshow("img",img)

    key = cv2.waitKey(0)


    if (key & 0xFF) == ord('q'):
        print(123)
        break
    elif(key & 0xFF == ord('s')):
        print('s')
        cv2.imwrite("/Users/xkzhai/OpenCV_Python/img_test/writelena.jpg",img)
    else:
            print(key)

cv2.destroyAllWindows()
