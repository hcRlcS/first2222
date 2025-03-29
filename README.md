# first2222
  1丶安装oprncv模块：在命令调试窗口输入pip install TensorFlow -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python 自动下载opencv模块
 
  2丶安装Matplotlib模块：在python端口中输入pip install matplotlib 等待安装完成即可

  3丶使用
    （1）print（cv2.getVersionStrring（））#可查看opencv安装版本
    （2）import cv2  调用opencv模块
    
  代码作用  
    （1）读取图片文件
         a = cv2.imread("文件名.jpg")  图片给到a
    
    （2）打开图片窗口
         cv2.imshow（"文件名"，a）
         cv2.waitKey（）                          
    
    （3）提取图片灰度图(test02.08)
          gray = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
          输入类型已加载BGR彩色图像的（三维数组），内存占用较大，适用于图形后处理阶段
          gray = cv2.imread("文件名.jpg", cv2.IMREAD_GRAYSCALE)
          输入类型为文件路径，内存占用较小，适用于图像加载阶段

    （4）图片的裁剪（test03）
          crop = a[10:170, 40:200]
          先截取竖直长度10到170，再截取横长

    （5）图片的绘制（test04）
          颜色 (255, 0, 0)蓝色    (0, 255, 0)绿色    (0, 0, 255)红色     (255, 255, 255)白色
          import numpy as np  输入才能创建画布
          创建一个画布：a = np.zeros([300, 300, 3], dtype=np.uint8)
          画一条直线：cv2.line(a，（，），（，），（，，），2）   （图， 两点坐标， 颜色， 线宽单位像素）
          画矩形：cv2.rectangle(a, (, ) , (, ) ,  (, , ) , 2)
          画圆：cv2.circle(a, (, ), 半径， (, , ), 2)
          画字符串：cv2.putText(image, "hello", (150, 100), 0, 1, (255, 255, 255), 2, 1)
          (a,位置坐标，字体序号0为默认，缩放系数， 颜色， 粗细， 线条类型1为实线）
     
     （6）图片降噪
           高斯滤波：gauss = cv2.GaussianBlur(a, (5, 5), 0) （a，设置内核， 
           中值滤波：median = cv2.medianBlur(image, 5) 

    （7）特征点提取
          先转为灰度图后
          corners = cv2.goodFeaturesToTrack(gray, 500, 0.1, 10)
          （图， 最多获取500个点， 点的质量优于0.1， 特征点间距离）

    （8）图像特征扫描
          template = gray[75:105, 235:265]                                    
          match = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)     
          locations = np.where(match >= 0.9)                                  找出匹配系数大于0.9的匹配点
          先选定特征区域后由cv2.TM_CCOEFF_NORMED标准相关匹配算法找到特征相似图

    （9）梯度算法
          laplacian = cv2.Laplacian(gray, cv2.CV_64F)      #计算拉普拉斯边缘

          
