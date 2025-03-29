import cv2
import numpy as np

image = cv2.imread("poker.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

template = gray[75:105, 235:265]                                    #区域内包含一个菱形

match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)     #cv2.TM_CCOEFF_NORMED标准相关匹配算法
locations = np.where(match >= 0.9)                                  #找出匹配系数大于0.9的匹配点

h, w = template.shape[0:2]       #求模板图案的长与宽
for p in zip(*locations[::-1]):  #在原始图像上画出对应的矩形框
    x1, y1 = p[0], p[1]
    x2, y2 = x1 + w, y1 +h
    cv2.rectangle(image, (x1, y1), (x2, y2),(0, 255, 0),2)

cv2.imshow("image", image)
cv2.waitKey()