# Image Steganography Tool
A Python and OpenCV-based image steganography tool that supports embedding QR codes into images and extracting embedded QR codes from images. The software provides a user-friendly graphical interface, suitable for beginners and general users.

## Features
### 1. Hide QR Code
Embed a selected QR code into a chosen image.
Supports input image formats:` .jpg, .png, .bmp, `and `.tiff`
The output image is saved in `.png` format.
### 2. Extract QR Code
Extract the embedded QR code from an image.
The extracted QR code is saved as a `.png` file.
## User Interface
The tool provides a simple graphical user interface (GUI) for the following actions:

**Hide QR Code:** Select an image and a QR code to embed, then save the result.
**Extract QR Code:** Select an image with an embedded QR code, then save the extracted QR code.
## Usage
### 1. Setup
This software is built with Python and requires the following dependencies:
`opencv-python`
`tkinter`

To install the dependencies, run:
`pip install opencv-python`
### 2. Running the Program
Run the main.py script to start the application:
`python Combine.py`
## Instructions
### Hide QR Code
Click the "Hide QR Code" button.
Select the original image and the QR code image.
Choose a save location and click "Save" to complete the process.
### Extract QR Code
Click the "Extract QR Code" button.
Select the image with the embedded QR code.
Choose a save location and click "Save" to complete the process.
## Example
![origin.jpg](./Example/origin.jpg#pic_center=300x300)

<p align="center">origin.jpg</p>

![dst.png](./Example/dst.png#pic_center=300x300)

<p align="center">dst.png</p>

![qr.png](./Example/qr.png#pic_center=300x300)

<p align="center">qr.png</p>

![extract_qr.png](./Example/extract_qr.png#pic_center=300x300)

<p align="center">extract_qr.png</p>

## Supported Image Formats
Input: `.jpg, .png, .bmp, .tiff`
Output: `.png`
## Notes
Make sure to have a backup of the original image.
The QR code will be embedded on top of the image, potentially covering part of the image content.
Ensure the input QR code image is clear and properly formatted.
## Developer
Developer: Cheri Wen
## Contact
Contact: [cherii8014@gmail.com]
## License
This project is licensed under the Apache License 2.0. You may use, modify, and distribute the software under the terms of the license.

You can find the full text of the Apache License 2.0 here: [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

Feel free to reach out for any further expansions or improvements you’d like to suggest!

**Let me know if you need any changes!**