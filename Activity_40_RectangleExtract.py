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
start_point = (50, 50)
end_point = (200, 200)
color = (0, 0, 255)
thickness = 2
rect_img = cv2.rectangle(img.copy(), start_point, end_point, color, thickness)
cv2.imwrite("C:\\Users\\habee\\OpenCV\\Activity_40_rect_image.jpg", rect_img)
cv2.imshow('Image with Rectangle', rect_img)
cv2.waitKey(0)
obj_img = img[start_point[1]:end_point[1], start_point[0]:end_point[0]]
cv2.imwrite("C:\\Users\\habee\\OpenCV\\Activity_40_object.jpg", obj_img)
cv2.imshow('Extracted Object', obj_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
