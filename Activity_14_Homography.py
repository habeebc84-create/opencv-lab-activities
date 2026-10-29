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
dst_points = np.float32([[0, 0], [cols - 1, 0], [0, int(0.7*rows)], [cols - 1, int(0.7*rows)]])
M, _ = cv2.findHomography(src_points, dst_points)
homography_img = cv2.warpPerspective(img, M, (cols, rows))
cv2.imwrite("C:\\Users\\habee\\OpenCV\\Activity_14_transformation_using_Homography_Image.jpg", homography_img)
cv2.imshow('Homography', homography_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
