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

img = cv2.imread("C:\\Users\\habee\\OpenCV\\image1.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)
dilated_img = cv2.dilate(img, kernel, iterations=1)
cv2.imwrite("C:\\Users\\habee\\OpenCV\\Dilated_Image.jpg", dilated_img)
cv2.imshow('Dilated Image', dilated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
