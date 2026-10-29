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
rows, cols = img.shape[:2]
src_points = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])
dst_points = np.float32([[0, 0], [cols - 1, 0], [int(0.33*cols), rows - 1], [int(0.66*cols), rows - 1]])
M = cv2.getPerspectiveTransform(src_points, dst_points)
perspective_img = cv2.warpPerspective(img, M, (cols, rows))
cv2.imwrite("C:\\Users\\habee\\OpenCV\\Perspective_Transformed_Image.jpg", perspective_img)
cv2.imshow('Perspective', perspective_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
