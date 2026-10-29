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

# Add salt-and-pepper noise
noisy = img.copy()
prob = 0.05
rnd = np.random.rand(*img.shape)
noisy[rnd < prob/2] = 0
noisy[rnd > 1 - prob/2] = 255
cv2.imwrite('C:\\Users\\habee\\OpenCV\\act3_noisy.jpg', noisy)

# 1. 3x3 Mean filter
mean3 = cv2.blur(noisy, (3, 3))
# 2. 5x5 Mean filter
mean5 = cv2.blur(noisy, (5, 5))
# 3. 3x3 Median filter
median3 = cv2.medianBlur(noisy, 3)
# 4. Gaussian filter
gauss = cv2.GaussianBlur(noisy, (5, 5), 1.0)

cv2.imwrite('C:\\Users\\habee\\OpenCV\\act3_mean3.jpg', mean3)
cv2.imwrite('C:\\Users\\habee\\OpenCV\\act3_mean5.jpg', mean5)
cv2.imwrite('C:\\Users\\habee\\OpenCV\\act3_median3.jpg', median3)
cv2.imwrite('C:\\Users\\habee\\OpenCV\\act3_gaussian.jpg', gauss)

titles = ['Noisy', 'Mean 3x3', 'Mean 5x5', 'Median 3x3', 'Gaussian']
images = [noisy, mean3, mean5, median3, gauss]
fig, axes = plt.subplots(1, 5, figsize=(18, 4))
for ax, im, t in zip(axes, images, titles):
    ax.imshow(im, cmap='gray', vmin=0, vmax=255)
    ax.set_title(t)
    ax.axis('off')
plt.tight_layout()
plt.savefig('C:\\Users\\habee\\OpenCV\\act3_smoothing.png', dpi=100)
plt.close()
print("Activity 3 done. Saved act3_smoothing.png + outputs.")
