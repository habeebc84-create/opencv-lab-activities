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

# Read grayscale image
img = cv2.imread('C:\\Users\\habee\\OpenCV\\image1.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (256, 256))

L = 256  # gray levels

# 1. Image negative
neg = L - 1 - img

# 2. Logarithmic transformation
c_log = (L - 1) / np.log(1 + int(np.max(img)))
log_img = c_log * np.log(1 + img.astype(np.float64))
log_img = np.uint8(np.clip(log_img, 0, L - 1))

# 3. Power-law (Gamma) transformation
def gamma_transform(image, gamma):
    c = (L - 1) / ((L - 1) ** gamma) if (L-1)**gamma != 0 else 1
    out = c * (image.astype(np.float64) ** gamma)
    return np.uint8(np.clip(out, 0, L - 1))

gamma_05 = gamma_transform(img, 0.5)
gamma_20 = gamma_transform(img, 2.0)

# 4. Contrast stretching
r_min, r_max = img.min(), img.max()
if r_max - r_min == 0:
    stretch = img.copy()
else:
    stretch = ((img.astype(np.float64) - r_min) / (r_max - r_min)) * (L - 1)
stretch = np.uint8(np.clip(stretch, 0, L - 1))

# Save individual outputs
cv2.imwrite('C:\\Users\\habee\\OpenCV\\act1_negative.jpg', neg)
cv2.imwrite('C:\\Users\\habee\\OpenCV\\act1_log.jpg', log_img)
cv2.imwrite('C:\\Users\\habee\\OpenCV\\act1_gamma_0.5.jpg', gamma_05)
cv2.imwrite('C:\\Users\\habee\\OpenCV\\act1_gamma_2.0.jpg', gamma_20)
cv2.imwrite('C:\\Users\\habee\\OpenCV\\act1_contrast_stretch.jpg', stretch)

# Side-by-side display
titles = ['Original', 'Negative', 'Log', 'Gamma 0.5', 'Gamma 2.0', 'Contrast Stretch']
images = [img, neg, log_img, gamma_05, gamma_20, stretch]

fig, axes = plt.subplots(2, 3, figsize=(12, 8))
for ax, im, t in zip(axes.flatten(), images, titles):
    ax.imshow(im, cmap='gray', vmin=0, vmax=255)
    ax.set_title(t)
    ax.axis('off')
plt.tight_layout()
plt.savefig('C:\\Users\\habee\\OpenCV\\act1_comparison.png', dpi=100)
plt.close()
print("Activity 1 done. Saved act1_comparison.png + individual outputs.")
