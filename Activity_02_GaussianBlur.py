import sys, os
try:
    import cv2
except ModuleNotFoundError:
    _py = r"C:\Users\habee\AppData\Local\Programs\Python\Python313\python.exe"
    if os.path.exists(_py) and os.path.abspath(sys.executable).lower() != os.path.abspath(_py).lower():
        os.execv(_py, [_py] + sys.argv)
    raise
import cv2

image = cv2.imread("C:\\Users\\habee\\OpenCV\\image1.jpg")
blur = cv2.GaussianBlur(image, (5, 5), 10)
cv2.imwrite("C:\\Users\\habee\\OpenCV\\Activity_02_blurred_image.jpg", blur)
cv2.imshow('Blurred Image', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
