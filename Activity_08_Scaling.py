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
height, width = image.shape[:2]

scale_factor = 3.0
bigger_image = cv2.resize(image, (int(width * scale_factor), int(height * scale_factor)))

scale_factor = 0.5
smaller_image = cv2.resize(image, (int(width * scale_factor), int(height * scale_factor)))

cv2.imshow('original image', image)
cv2.imshow('Bigger image', bigger_image)
cv2.imshow('smaller image', smaller_image)

cv2.imwrite("C:\\Users\\habee\\OpenCV\\Bigger_image.jpg", bigger_image)
cv2.imwrite("C:\\Users\\habee\\OpenCV\\smaller_image.jpg", smaller_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
