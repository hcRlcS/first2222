import cv2
print(cv2.getVersionString())         #print opencv版本

image = cv2.imread("opencv_logo.jpg") #使用openCV读取图片文件
print(image.shape)                    #打印图片维度：有三个维度（图片像素横行，纵行，图片三原色彩色通道）

cv2.imshow("image",image)             #打开图片网口
cv2.waitKey()                         #使窗口常开，输入任意键后取消
