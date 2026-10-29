import sys, os
try:
    import cv2
except ModuleNotFoundError:
    _py = r"C:\Users\habee\AppData\Local\Programs\Python\Python313\python.exe"
    if os.path.exists(_py) and os.path.abspath(sys.executable).lower() != os.path.abspath(_py).lower():
        os.execv(_py, [_py] + sys.argv)
    raise
import cv2
import numpy as np

def high_boost_filter(image, boost_factor):
    kernel_size = 3
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size ** 2)
    blur_image = cv2.filter2D(image, -1, kernel)
    mask = image + (image - blur_image) * boost_factor
    return mask

image = cv2.imread("C:\\Users\\habee\\OpenCV\\image1.jpg")
sharpened_image = high_boost_filter(image, 1.5)
cv2.imwrite("C:\\Users\\habee\\OpenCV\\sharpened_image.jpg", sharpened_image)
cv2.imshow('HighBoost', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
