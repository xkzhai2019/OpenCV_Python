import cv2

cv2.namedWindow("img",cv2.WINDOW_NORMAL)

img = cv2.imread("../OpenCV_Python/img/lena.jpg")

cv2.imshow("img",img)

key = cv2.waitKey(0)
print(key)

print('q')
print(ord('q'))

if (key & 0xFF) == ord('q'):
    print(1111)
    cv2.destroyAllWindows()