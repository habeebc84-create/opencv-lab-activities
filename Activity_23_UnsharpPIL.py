import sys, os
try:
    import cv2
except ModuleNotFoundError:
    _py = r"C:\Users\habee\AppData\Local\Programs\Python\Python313\python.exe"
    if os.path.exists(_py) and os.path.abspath(sys.executable).lower() != os.path.abspath(_py).lower():
        os.execv(_py, [_py] + sys.argv)
    raise
from PIL import Image, ImageFilter

image_path = "C:\\Users\\habee\\OpenCV\\image1.jpg"
im1 = Image.open(image_path)
im2 = im1.filter(ImageFilter.UnsharpMask(radius=3, percent=200, threshold=5))
im2.save("C:\\Users\\habee\\OpenCV\\unsharp_pil.jpg")
im2.show()
