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

# Low-contrast grayscale image
img = cv2.imread('C:\\Users\\habee\\OpenCV\\image1.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (256, 256))

# Reference image for histogram matching (use a contrast-stretched version as reference)
ref = cv2.equalizeHist(img.copy())
# make reference a bit different: use gamma
ref = np.uint8(np.clip((ref.astype(np.float64)/255.0)**0.8 * 255, 0, 255))

def hist_match(source, reference):
    # Compute CDFs
    src_hist, _ = np.histogram(source.flatten(), 256, [0, 256])
    ref_hist, _ = np.histogram(reference.flatten(), 256, [0, 256])
    src_cdf = np.cumsum(src_hist).astype(np.float64)
    ref_cdf = np.cumsum(ref_hist).astype(np.float64)
    src_cdf /= src_cdf[-1]
    ref_cdf /= ref_cdf[-1]
    # Map each gray level
    mapping = np.zeros(256, dtype=np.uint8)
    for i in range(256):
        # find j such that ref_cdf[j] >= src_cdf[i]
        j = np.searchsorted(ref_cdf, src_cdf[i])
        if j >= 256:
            j = 255
        mapping[i] = j
    return mapping[source]

# 1. Histogram calculation (just compute)
hist_orig = cv2.calcHist([img], [0], None, [256], [0, 256])

# 2. Histogram equalization
eq = cv2.equalizeHist(img)

# 3. Histogram specification/matching
matched = hist_match(img, ref)

cv2.imwrite('C:\\Users\\habee\\OpenCV\\act2_equalized.jpg', eq)
cv2.imwrite('C:\\Users\\habee\\OpenCV\\act2_matched.jpg', matched)
cv2.imwrite('C:\\Users\\habee\\OpenCV\\act2_reference.jpg', ref)

# Plot histograms before and after
fig, axes = plt.subplots(3, 2, figsize=(12, 10))
pairs = [('Original', img), ('Equalized', eq), ('Matched', matched)]
for i, (title, im) in enumerate(pairs):
    axes[i, 0].imshow(im, cmap='gray', vmin=0, vmax=255)
    axes[i, 0].set_title(title)
    axes[i, 0].axis('off')
    h = cv2.calcHist([im], [0], None, [256], [0, 256])
    axes[i, 1].plot(h, color='black')
    axes[i, 1].set_title(title + ' Histogram')
    axes[i, 1].set_xlim([0, 256])
plt.tight_layout()
plt.savefig('C:\\Users\\habee\\OpenCV\\act2_histograms.png', dpi=100)
plt.close()
print("Activity 2 done. Saved act2_histograms.png + outputs.")
