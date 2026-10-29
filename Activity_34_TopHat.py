import sys, os
try:
    import cv2
except ModuleNotFoundError:
    _py = r"C:\Users\habee\AppData\Local\Programs\Python\Python313\python.exe"
    if os.path.exists(_py) and os.path.abspath(sys.executable).lower() != os.path.abspath(_py).lower():
        os.execv(_py, [_py] + sys.argv)
    raise
import cv2

filterSize = (3, 3)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filterSize)
input_image = cv2.imread("C:\\Users\\habee\\OpenCV\\image1.jpg")
input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
tophat_img = cv2.morphologyEx(input_image, cv2.MORPH_TOPHAT, kernel)
cv2.imwrite("C:\\Users\\habee\\OpenCV\\Activity_34_tophat.jpg", tophat_img)
cv2.imshow('Top Hat', tophat_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
