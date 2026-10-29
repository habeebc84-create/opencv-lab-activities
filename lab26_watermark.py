import sys, os
try:
    import cv2
except ModuleNotFoundError:
    _py = r"C:\Users\habee\AppData\Local\Programs\Python\Python313\python.exe"
    if os.path.exists(_py) and os.path.abspath(sys.executable).lower() != os.path.abspath(_py).lower():
        os.execv(_py, [_py] + sys.argv)
    raise
import cv2
import math

logo = cv2.imread("C:\\Users\\habee\\OpenCV\\image1.jpg")
img = cv2.imread("C:\\Users\\habee\\OpenCV\\image2.jpg")
h_logo, w_logo = logo.shape[:2]
h_img, w_img = img.shape[:2]
center_y = int(h_img / 2)
center_x = int(w_img / 2)
top_y = center_y - int(h_logo / 2)
left_x = center_x - int(w_logo / 2)
bottom_y = top_y + h_logo
right_x = left_x + w_logo

# resize logo if needed to fit
if bottom_y > h_img or right_x > w_img:
    logo = cv2.resize(logo, (w_img // 2, h_img // 2))
    h_logo, w_logo = logo.shape[:2]
    top_y = center_y - int(h_logo / 2)
    left_x = center_x - int(w_logo / 2)
    bottom_y = top_y + h_logo
    right_x = left_x + w_logo

destination = img[top_y:bottom_y, left_x:right_x]
result = cv2.addWeighted(destination, 1, logo, 0.5, 0)
img[top_y:bottom_y, left_x:right_x] = result
cv2.imwrite("C:\\Users\\habee\\OpenCV\\watermarked.jpg", img)
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
