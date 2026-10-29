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
cv2.imshow("Original Image", image)
cv2.moveWindow("Original Image", 200, 200)
cv2.waitKey(0)
cv2.destroyAllWindows()
