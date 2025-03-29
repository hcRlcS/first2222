import cv2

image = cv2.imread("opencv_logo.jpg")

crop = image[10:170, 40:200]                      #对图片进行裁剪 先竖后横  10：170为第10横行到第170横行

cv2.imshow("crop", crop)
cv2.waitKey()
