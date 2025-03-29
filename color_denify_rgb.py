import cv2
import numpy as np

# 读取图像
image = cv2.imread("/home/zxz/work/opencv_test/normal_images/0_cropped.jpg")  # 替换为你的图片路径

# 定义红色的RGB范围
lower_red = np.array([0, 0, 100])   # 最低红色阈值
upper_red = np.array([100, 100, 255])  # 最高红色阈值

# 定义绿色的RGB范围
lower_green = np.array([0, 100, 0])
upper_green = np.array([100, 255, 100])

# 定义黄色的RGB范围
lower_yellow = np.array([0, 100, 100])
upper_yellow = np.array([100, 255, 255])

# 定义白色的RGB范围
lower_white = np.array([200, 200, 200])  # 白色通常具有高亮度
upper_white = np.array([255, 255, 255])

# 定义黑色的RGB范围
lower_black = np.array([0, 0, 0])    # 黑色通常具有低亮度
upper_black = np.array([30, 30, 30])

# 创建红色掩码
red_mask = cv2.inRange(image, lower_red, upper_red)

# 创建绿色掩码
green_mask = cv2.inRange(image, lower_green, upper_green)

# 创建黄色掩码
yellow_mask = cv2.inRange(image, lower_yellow, upper_yellow)

# 创建白色掩码
white_mask = cv2.inRange(image, lower_white, upper_white)

# 创建黑色掩码
black_mask = cv2.inRange(image, lower_black, upper_black)

# 合并所有颜色的掩码
combined_mask = cv2.bitwise_or(red_mask, cv2.bitwise_or(green_mask, cv2.bitwise_or(yellow_mask, cv2.bitwise_or(white_mask, black_mask))))

# 应用掩码到原始图像
combined_result = cv2.bitwise_and(image, image, mask=combined_mask)

# 显示结果
cv2.imshow("Original Image", image)
cv2.imshow("Combined Mask", combined_mask)
cv2.imshow("Combined Result", combined_result)

# 按下 'q' 键退出
key = cv2.waitKey(0)
if key == ord('q'):
    cv2.destroyAllWindows()