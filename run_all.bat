@echo off
cd /d "C:\Users\habee\OpenCV"
set PY=C:\Users\habee\AppData\Local\Programs\Python\Python313\python.exe
echo Running image-based lab activities...
"%PY%" Activity_01_Grayscale.py
"%PY%" Activity_02_GaussianBlur.py
"%PY%" Activity_03_CannyEdges.py
"%PY%" Activity_04_Dilate.py
"%PY%" Activity_05_Erode.py
"%PY%" Activity_08_Scaling.py
"%PY%" Activity_09_Rotation.py
"%PY%" Activity_10_MoveWindow.py
"%PY%" Activity_11_Affine.py
"%PY%" Activity_12_Perspective.py
"%PY%" Activity_14_Homography.py
"%PY%" Activity_16_Canny.py
"%PY%" Activity_17_SobelX.py
"%PY%" Activity_18_SobelY.py
"%PY%" Activity_19_SobelXY.py
"%PY%" Activity_20_LaplacianNeg.py
"%PY%" Activity_21_LaplacianDiag.py
"%PY%" Activity_22_LaplacianPos.py
"%PY%" Activity_23_UnsharpPIL.py
"%PY%" Activity_24_HighBoost.py
"%PY%" Activity_25_GradientMasking.py
"%PY%" Activity_26_Watermark.py
"%PY%" Activity_27_CropCopyPaste.py
"%PY%" Activity_28_ConvolutionBoundary.py
"%PY%" Activity_29_ErosionMorph.py
"%PY%" Activity_30_DilationMorph.py
"%PY%" Activity_31_Opening.py
"%PY%" Activity_32_Closing.py
"%PY%" Activity_33_MorphGradient.py
"%PY%" Activity_34_TopHat.py
"%PY%" Activity_35_BlackHat.py
"%PY%" Activity_40_RectangleExtract.py
echo.
echo NOTE: Activity_06, 07, 13, 37, 38 need a video file or webcam.
echo Done.
pause
