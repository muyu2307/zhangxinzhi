import cv2
import numpy as np
  
# 读取图像
#image0 = cv2.imread("/home/zxz/work/opencv_test/normal_images/0_cropped.jpg")  # 替换为你的图片路径
#image1 = cv2.imread("/home/zxz/work/opencv_test/normal_images/1_cropped.jpg") 
#image2 = cv2.imread("/home/zxz/work/opencv_test/normal_images/2_cropped.jpg") 
#image3 = cv2.imread("/home/zxz/work/opencv_test/normal_images/3_cropped.jpg") 
#image4 = cv2.imread("/home/zxz/work/opencv_test/normal_images/4_cropped.jpg") 
image0 = cv2.imread("/home/zxz/work/opencv_test/stronglight_images/0_cropped.jpg") 
# 将图像从BGR颜色空间转换到HSV颜色空间
hsv_image = cv2.cvtColor(image0, cv2.COLOR_BGR2HSV)
#hsv_image = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
#hsv_image = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)
#hsv_image = cv2.cvtColor(image3, cv2.COLOR_BGR2HSV)
#hsv_image = cv2.cvtColor(image4, cv2.COLOR_BGR2HSV) 



# 定义红色的HSV范围
# 注意：HSV中红色的H值范围是[0, 10]和[170, 180]，因为红色在HSV色环的两端
lower_red1 = np.array([0, 50, 50])   # 红色范围1
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 50, 50]) # 红色范围2
upper_red2 = np.array([180, 255, 255])

# 定义红色的HSV范围
lower_red1 = np.array([0, 50, 50])   # 红色范围1
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 50, 50]) # 红色范围2
upper_red2 = np.array([180, 255, 255])

# 定义绿色的HSV范围
lower_green = np.array([35, 50, 50])
upper_green = np.array([85, 255, 255])

# 定义黄色的HSV范围
lower_yellow = np.array([20, 50, 50])
upper_yellow = np.array([35, 255, 255])

# 定义白色的HSV范围
lower_white = np.array([0, 0, 200])  # 白色通常具有高亮度（Value）
upper_white = np.array([180, 30, 255])

# 定义黑色的HSV范围
lower_black = np.array([0, 0, 0])    # 黑色通常具有低亮度（Value）
upper_black = np.array([180, 255, 30])

# 创建红色掩码
red_mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
red_mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(red_mask1, red_mask2)

# 创建绿色掩码
green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

# 创建黄色掩码
yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

# 创建白色掩码
white_mask = cv2.inRange(hsv_image, lower_white, upper_white)

# 创建黑色掩码
black_mask = cv2.inRange(hsv_image, lower_black, upper_black)

# 合并所有颜色的掩码
combined_mask = cv2.bitwise_or(red_mask, cv2.bitwise_or(green_mask, cv2.bitwise_or(yellow_mask, cv2.bitwise_or(white_mask, black_mask))))



combined_result0 = cv2.bitwise_and(image0, image0, mask=combined_mask)
#combined_result1 = cv2.bitwise_and(image1, image1, mask=combined_mask)
#combined_result2 = cv2.bitwise_and(image2, image2, mask=combined_mask)
#combined_result3 = cv2.bitwise_and(image3, image3, mask=combined_mask)
#combined_result4 = cv2.bitwise_and(image4, image4, mask=combined_mask)

# 显示结果
cv2.imshow("Original Image0", image0)
#cv2.imshow("Original Image1", image1)
#cv2.imshow("Original Image2", image2)
#cv2.imshow("Original Image3", image3)
#cv2.imshow("Original Image4", image4)

cv2.imshow("Mask",combined_mask)
cv2.imshow("Result0", combined_result0)
#cv2.imshow("Result1", combined_result1)
#cv2.imshow("Result2", combined_result2)
#cv2.imshow("Result3", combined_result3)
#cv2.imshow("Result4", combined_result4)

cv2.waitKey(0)
cv2.destroyAllWindows()


