'''
import cv2
import qrcode
import numpy as np


def write(content, img_path, save_path="qr.png"):
    """在图片中隐写二维码"""
    # # 生成二维码
    img = qrcode.make(content)
    qr = np.array(img, dtype=np.uint8)
    # # 读取图片
    img = cv2.imread(img_path)
    b = img[:, :, 0]
    # # 将最低位平面数值清0
    bit1 = cv2.bitwise_and(b, 1)
    b -= bit1
    # # 将二维码转换成和图片一个形状
    qr = cv2.resize(qr, b.shape)
    # 将二维码隐藏到最低位平面
    img[:, :, 0] = b + qr
    # 保存图片需要png后缀
    cv2.imwrite(save_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])  # 无损


def read(imagepath, qrpath="qr.jpg"):
    """读取隐写内容"""
    im = cv2.imread(imagepath)
    img = cv2.bitwise_and(im[:, :, 0], 1)
    _, dst = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
    cv2.imwrite(qrpath, dst)


if __name__ == '__main__':
    write("公众号：新建文件夹", "alice.jpg")
    read("qr.png")

'''

import cv2
import numpy as np

# ①读取图像
img = cv2.imread('E:\Projects\PicLock\\alice.jpg', 0)

# ②把最低有效位清空
img -= cv2.bitwise_and(img, 0x01)

# ③准备需要隐写的信息M
M = cv2.imread('E:\Projects\PicLock\qr.jpg', 0)
M = cv2.resize(M, img.shape)

# 把二维码转换成0-1矩阵
_, M = cv2.threshold(M, 30, 1, cv2.THRESH_BINARY)

# ④将要隐写的数据设置到图像最低有效位
M = np.reshape(M, img.shape)
img += M

# ⑥以无损的方式保存隐写后的
cv2.imwrite('E:\Projects\PicLock\dst.png', img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
