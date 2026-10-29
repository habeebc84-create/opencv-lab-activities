@echo off
cd /d "C:\Users\habee\OpenCV"
set PY=C:\Users\habee\AppData\Local\Programs\Python\Python313\python.exe
echo Running image-based lab activities...
"%PY%" lab01_grayscale.py
"%PY%" lab02_gaussian_blur.py
"%PY%" lab03_canny_edges.py
"%PY%" lab04_dilate.py
"%PY%" lab05_erode.py
"%PY%" lab08_scaling.py
"%PY%" lab09_rotation.py
"%PY%" lab10_move_window.py
"%PY%" lab11_affine.py
"%PY%" lab12_perspective.py
"%PY%" lab14_homography.py
"%PY%" lab16_canny.py
"%PY%" lab17_sobel_x.py
"%PY%" lab18_sobel_y.py
"%PY%" lab19_sobel_xy.py
"%PY%" lab20_laplacian_neg.py
"%PY%" lab21_laplacian_diag.py
"%PY%" lab22_laplacian_pos.py
"%PY%" lab23_unsharp_pil.py
"%PY%" lab24_highboost.py
"%PY%" lab25_gradient_masking.py
"%PY%" lab26_watermark.py
"%PY%" lab27_crop_copypaste.py
"%PY%" lab28_convolution_boundary.py
"%PY%" lab29_erosion_morph.py
"%PY%" lab30_dilation_morph.py
"%PY%" lab31_opening.py
"%PY%" lab32_closing.py
"%PY%" lab33_morph_gradient.py
"%PY%" lab34_tophat.py
"%PY%" lab35_blackhat.py
"%PY%" lab40_rectangle_extract.py
echo.
echo NOTE: lab06, lab07, lab13, lab37, lab38 need a video file or webcam.
echo Done.
pause
