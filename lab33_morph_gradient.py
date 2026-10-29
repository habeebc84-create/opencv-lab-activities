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

img = cv2.imread("C:\\Users\\habee\\OpenCV\\image1.jpg", 0)
kernel = np.ones((3, 3), np.uint8)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imwrite("C:\\Users\\habee\\OpenCV\\Morphological_Gradient.jpg", gradient)
cv2.imshow('Morph Gradient', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
