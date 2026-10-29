import sys, os
try:
    import cv2
except ModuleNotFoundError:
    _py = r"C:\Users\habee\AppData\Local\Programs\Python\Python313\python.exe"
    if os.path.exists(_py) and os.path.abspath(sys.executable).lower() != os.path.abspath(_py).lower():
        os.execv(_py, [_py] + sys.argv)
    raise
import cv2

# Cropping
img = cv2.imread("C:\\Users\\habee\\OpenCV\\image1.jpg")
crop_img = img[10:300, 10:300]
cv2.imwrite("C:\\Users\\habee\\OpenCV\\Activity_27_cropped.jpg", crop_img)
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)

# Copy and paste
img1 = cv2.imread("C:\\Users\\habee\\OpenCV\\image1.jpg")
img2 = cv2.imread("C:\\Users\\habee\\OpenCV\\image2.jpg")
rows, cols = img2.shape[:2]
roi = img1[50:50+rows, 50:50+cols]
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
dst = cv2.add(img1_bg, img2_fg)
img1[50:50+rows, 50:50+cols] = dst
cv2.imwrite("C:\\Users\\habee\\OpenCV\\Activity_27_copy_paste.jpg", img1)
cv2.imshow('result', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
