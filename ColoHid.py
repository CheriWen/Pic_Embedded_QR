import cv2 as np
import numpy as cv2
import os

# Read the image and QR code
img_path = r'E:\Projects\PicLock\origin.jpg'
qr_path = r'E:\Projects\PicLock\qr.jpg'
output_path = r'E:\Projects\PicLock\dst.png'

img = np.imread(img_path)
M = np.imread(qr_path)

# Check if the file is read successfully
if img is None or M is None:
    raise FileNotFoundError("Image or QR file not found!")

# Resize the QR code image
M = np.resize(M, (img.shape[1], img.shape[0]), interpolation=np.INTER_AREA)

# Convert to grayscale and binarize
M_binary = np.cvtColor(M, np.COLOR_BGR2GRAY)
_, M_binary = np.threshold(M_binary, 127, 1, np.THRESH_BINARY)

# Expand the binarized information to three channels
M_colored = cv2.repeat(M_binary[:, :, cv2.newaxis], 3, axis=2)

# Embed information into the least significant bit
img = img & ~1  # Clear the least significant bit
img = img | M_colored  # Embed information

# Save the stego image
np.imwrite(output_path, img, [np.IMWRITE_PNG_COMPRESSION, 0])
