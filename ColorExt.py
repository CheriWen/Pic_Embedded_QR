import cv2 as np
import numpy as cv2

# Read the stego image
stego_img_path = r'E:\Projects\PicLock\dst.png'
output_qr_path = r'E:\Projects\PicLock\extracted_qr.png'

stego_img = np.imread(stego_img_path)

# Check if the file is read successfully
if stego_img is None:
    raise FileNotFoundError("Stego image file not found!")

# Extract the least significant bit
extracted_bits = stego_img & 1

# Convert the least significant bit of each channel to a single channel (grayscale)
extracted_qr = extracted_bits[:, :, 0] * 255  

# Save the extracted QR code image
np.imwrite(output_qr_path, extracted_qr)

print(f"QR code extraction completed, saved path: {output_qr_path}")
