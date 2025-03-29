
import cv2

image = cv2.imread("opencv_logo.jpg")

cv2.imshow("blue", image[:, :, 0])
cv2.imshow("red",image[:,:,2])
cv2.imshow("green",image[:, :, 1])     #提取灰度图  显示在blue red green三个窗口中

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)   #彩色图像的灰度变换算法 ，得出的图像为灰度图
cv2.imshow("gray", gray)

cv2.waitKey()
