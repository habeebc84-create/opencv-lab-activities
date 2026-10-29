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

img = cv2.imread("C:\\Users\\habee\\OpenCV\\image1.jpg")
kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
sharpened = cv2.filter2D(img, -1, kernel)
cv2.imwrite("C:\\Users\\habee\\OpenCV\\Sharpened_Image.jpg", sharpened)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
