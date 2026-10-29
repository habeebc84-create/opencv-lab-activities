import sys, os
try:
    import cv2
except ModuleNotFoundError:
    _py = r"C:\Users\habee\AppData\Local\Programs\Python\Python313\python.exe"
    if os.path.exists(_py) and os.path.abspath(sys.executable).lower() != os.path.abspath(_py).lower():
        os.execv(_py, [_py] + sys.argv)
    raise
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

img = cv2.imread('C:\\Users\\habee\\OpenCV\\image1.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (256, 256))
# blurred/low-detail input
blurred = cv2.GaussianBlur(img, (9, 9), 2.0)
cv2.imwrite('C:\\Users\\habee\\OpenCV\\act4_blurred_input.jpg', blurred)

# 1. Laplacian filter
lap = cv2.Laplacian(blurred, cv2.CV_64F)
sharpened_lap = np.clip(blurred.astype(np.float64) - lap, 0, 255).astype(np.uint8)

# 2. Sobel operator
sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
mag = np.sqrt(sobelx**2 + sobely**2)
mag = np.uint8(np.clip(mag, 0, 255))
sharpened_sobel = np.clip(blurred.astype(np.int32) + mag.astype(np.int32), 0, 255).astype(np.uint8)

# 3. High-pass spatial filtering
hp_kernel = np.array([[-1, -1, -1],
                      [-1,  8, -1],
                      [-1, -1, -1]], dtype=np.float32)
hp = cv2.filter2D(blurred, cv2.CV_64F, hp_kernel)
sharpened_hp = np.clip(blurred.astype(np.float64) + hp, 0, 255).astype(np.uint8)

# 4. Unsharp masking
gauss = cv2.GaussianBlur(blurred, (9, 9), 2.0)
mask = blurred.astype(np.float64) - gauss.astype(np.float64)
sharpened_unsharp = np.clip(blurred.astype(np.float64) + 1.5 * mask, 0, 255).astype(np.uint8)

cv2.imwrite('C:\\Users\\habee\\OpenCV\\act4_laplacian.jpg', sharpened_lap)
cv2.imwrite('C:\\Users\\habee\\OpenCV\\act4_sobel.jpg', sharpened_sobel)
cv2.imwrite('C:\\Users\\habee\\OpenCV\\act4_highpass.jpg', sharpened_hp)
cv2.imwrite('C:\\Users\\habee\\OpenCV\\act4_unsharp.jpg', sharpened_unsharp)

titles = ['Blurred (input)', 'Laplacian', 'Sobel', 'High-pass', 'Unsharp']
images = [blurred, sharpened_lap, sharpened_sobel, sharpened_hp, sharpened_unsharp]
fig, axes = plt.subplots(1, 5, figsize=(18, 4))
for ax, im, t in zip(axes, images, titles):
    ax.imshow(im, cmap='gray', vmin=0, vmax=255)
    ax.set_title(t)
    ax.axis('off')
plt.tight_layout()
plt.savefig('C:\\Users\\habee\\OpenCV\\act4_sharpening.png', dpi=100)
plt.close()
print("Activity 4 done. Saved act4_sharpening.png + outputs.")
