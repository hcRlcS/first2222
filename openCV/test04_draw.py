import cv2
import numpy as np

image = np.zeros([300, 300, 3], dtype=np.uint8)   #创建一个灰色画布 灰度的数值类型为无符号8位整数

cv2.line(image,(100, 200), (250, 250),(250, 0 ,0), 2)   #画一条直线（两个点的坐标，选择颜色，线粗）
cv2.rectangle(image, (30,100), (250,230), (0, 255, 0), 2)                       #画一个矩形框（两个对角坐标，颜色，线两个像素）
cv2.circle(image, (150, 100), 50, (0, 0, 255), 2)   #画圆
cv2.putText(image, "hello", (150, 100), 0, 1, (255, 255, 255), 2, 1)
                                     #(位置坐标，字体序号0为默认，缩放系数， 颜色， 粗细， 线条类型1为实线）
                                     #颜色值为255（blue，green，red）三个都为255时为白色
cv2.imshow("image", image)
cv2.waitKey()