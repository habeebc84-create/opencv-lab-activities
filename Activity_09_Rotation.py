import sys, os
try:
    import cv2
except ModuleNotFoundError:
    _py = r"C:\Users\habee\AppData\Local\Programs\Python\Python313\python.exe"
    if os.path.exists(_py) and os.path.abspath(sys.executable).lower() != os.path.abspath(_py).lower():
        os.execv(_py, [_py] + sys.argv)
    raise
import cv2

img = cv2.imread("C:\\Users\\habee\\OpenCV\\image1.jpg")
rotated_cw = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotated_ccw = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite("C:\\Users\\habee\\OpenCV\\rotated_cw.jpg", rotated_cw)
cv2.imwrite("C:\\Users\\habee\\OpenCV\\rotated_ccw.jpg", rotated_ccw)
cv2.imshow('Clockwise', rotated_cw)
cv2.imshow('CounterClockwise', rotated_ccw)
cv2.waitKey(0)
cv2.destroyAllWindows()
