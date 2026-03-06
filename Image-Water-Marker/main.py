from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    if file_path:
        print("Selected:", file_path)
        return file_path
    return None

def add_watermark():
    image_path = upload_image()
    if not image_path:
        print("No image selected!")
        return

    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 40)

    watermark_text = "anand"
    width, height = img.size
    text_position = (width - 200, height - 50)

    draw.text(text_position, watermark_text, fill="white", font=font)
    save_path = "watermarked_image.png"
    img.save(save_path)
    print(f"watermark added! Saved as: {save_path}")

window = Tk()
window.title("Image Watermark App")
window.geometry("400x200")

upload_btn = Button(window, text="Upload Image & Add Watermark", command=add_watermark)
upload_btn.pack(pady=50)

window.mainloop()