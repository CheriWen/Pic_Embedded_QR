import cv2
import numpy as np

# Read image
img = cv2.imread('E:\Projects\PicLock\\origin.jpg', 0)

# Clear the least significant bit
img -= cv2.bitwise_and(img, 0x01)

# Prepare the information to be hidden
M = cv2.imread('E:\Projects\PicLock\qr.jpg', 0)
M = cv2.resize(M, img.shape)

# Convert the QR code to a 0-1 matrix
_, M = cv2.threshold(M, 30, 1, cv2.THRESH_BINARY)

# Set the data to be hidden to the least significant bit of the image
M = np.reshape(M, img.shape)
img += M

# Save the stego image in lossless mode
cv2.imwrite('E:\Projects\PicLock\dst.png', img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
