import cv2
import numpy as np

# 读取隐写后的图像
stego_img = cv2.imread('E:\Projects\PicLock\dst.png', 0)

# 获取图像的最低有效位，即提取隐写的信息（这里是二维码）
extracted_info = cv2.bitwise_and(stego_img, 0x01)

# 将提取的信息转换为可显示的图像格式（这里将0和1矩阵转换为合适的灰度值范围）
extracted_img = np.uint8(extracted_info * 255)

# 保存提取出的二维码图像为新的文件
cv2.imwrite('E:\Projects\PicLock\extracted_qr.png', extracted_img)