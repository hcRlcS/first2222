import cv2

gray = cv2.imread("opencv_logo.jpg", cv2.IMREAD_GRAYSCALE)

laplacian = cv2.Laplacian(gray, cv2.CV_64F)      #计算拉普拉斯边缘

cv2.imshow("gray", gray)
cv2.imshow("laplacian", laplacian)

cv2.waitKey()