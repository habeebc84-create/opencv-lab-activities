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

image = cv2.imread("C:\\Users\\habee\\OpenCV\\image1.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gradient_x = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=3)
gradient_y = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=3)
gradient = cv2.subtract(gradient_x, gradient_y)
cv2.imwrite("C:\\Users\\habee\\OpenCV\\sharpened_image3.jpg", gradient)
cv2.imshow('Gradient', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
