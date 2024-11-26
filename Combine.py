import cv2
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Adjust Size
def resize_to_square(image, size):
    return cv2.resize(image, (size, size), interpolation=cv2.INTER_AREA)

# Hide QR Code
def hide_qr():
    try:
        # Disable Buttons
        btn_hide_qr.config(state=tk.DISABLED)
        btn_extract_qr.config(state=tk.DISABLED)
        
        # Select Files
        img_path = filedialog.askopenfilename(title="选择原始图片", filetypes=[("图片文件", "*.jpg;*.png;*.bmp;*.tiff")])
        if not img_path:
            return

        qr_path = filedialog.askopenfilename(title="选择二维码图片", filetypes=[("图片文件", "*.jpg;*.png;*.bmp;*.tiff")])
        if not qr_path:
            return

        output_path = filedialog.asksaveasfilename(title="保存嵌入后的图片", defaultextension=".png",
                                                   filetypes=[("PNG 文件", "*.png")])
        if not output_path:
            return

        # Read Images
        img = cv2.imread(img_path)
        M = cv2.imread(qr_path)
        if img is None or M is None:
            raise FileNotFoundError("无法读取图片文件！")

        # Adjust Size
        M = cv2.resize(M, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_AREA)

        # Convert To Binary
        M_binary = cv2.cvtColor(M, cv2.COLOR_BGR2GRAY)
        _, M_binary = cv2.threshold(M_binary, 127, 1, cv2.THRESH_BINARY)

        # Extend To 3 Channels
        M_colored = cv2.merge([M_binary] * 3)

        # Embed QR Code
        img = img & ~1  # Clear LSB
        img = img | M_colored  # Embed QR Code

        # Save Image
        cv2.imwrite(output_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        messagebox.showinfo("成功", f"图片成功保存到：{output_path}")
    except Exception as e:
        messagebox.showerror("错误", f"信息隐藏失败：{str(e)}")
    
    finally:
        # Enable Buttons
        btn_hide_qr.config(state=tk.NORMAL)
        btn_extract_qr.config(state=tk.NORMAL)

# Extract QR Code
def extract_qr():
    try:
        # Disable Buttons
        btn_hide_qr.config(state=tk.DISABLED)
        btn_extract_qr.config(state=tk.DISABLED)

        # Select Files
        stego_img_path = filedialog.askopenfilename(title="选择嵌入后的图片", filetypes=[("图片文件", "*.jpg;*.png;*.bmp;*.tiff")])
        if not stego_img_path:
            return

        output_qr_path = filedialog.asksaveasfilename(title="保存提取的二维码", defaultextension=".png",
                                                      filetypes=[("PNG 文件", "*.png")])
        if not output_qr_path:
            return

        # Read Embedded Image
        stego_img = cv2.imread(stego_img_path)
        if stego_img is None:
            raise FileNotFoundError("无法读取嵌入图片文件！")

        # Extract QR Code
        extracted_qr = (stego_img[:, :, 0] & 1) * 255  # Extract LSB And Convert to 255

        # Adjust Size
        size = min(stego_img.shape[:2])
        extracted_qr = resize_to_square(extracted_qr, size)

        # Save QR Code
        cv2.imwrite(output_qr_path, extracted_qr)
        messagebox.showinfo("成功", f"二维码成功保存到：{output_qr_path}")
    except Exception as e:
        messagebox.showerror("错误", f"信息提取失败：{str(e)}")

    finally:
        # Enable Buttons
        btn_hide_qr.config(state=tk.NORMAL)
        btn_extract_qr.config(state=tk.NORMAL)

# Main Window
def main():
    # Creat Window
    root = tk.Tk()
    root.title("图像隐写工具")
    root.geometry("400x300")

    # Set Theme
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), padding=10)
    style.configure("TLabel", font=("Arial", 14), padding=10)

    # Creat Title
    title_label = ttk.Label(root, text="图像隐写工具", anchor="center")
    title_label.pack(pady=20)

    # Creat Buttons
    global btn_hide_qr, btn_extract_qr

    btn_hide_qr = ttk.Button(root, text="隐藏二维码", command=hide_qr)
    btn_hide_qr.pack(pady=10)

    btn_extract_qr = ttk.Button(root, text="提取二维码", command=extract_qr)
    btn_extract_qr.pack(pady=10)

    # Creat Footer
    footer_label = ttk.Label(root, text="© Cheri Wen 2024", anchor="center")
    footer_label.pack(side="bottom", pady=10)

    # Run Main Loop
    root.mainloop()

# Run
if __name__ == "__main__":
    main()
