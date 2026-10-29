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

# NOTE: uses webcam. Press q to quit.
roi_points = np.array([(150, 200), (450, 200), (550, 500), (50, 500)])
target_points = np.array([(0, 0), (400, 0), (400, 600), (0, 600)])
M = cv2.getPerspectiveTransform(roi_points.astype(np.float32), target_points.astype(np.float32))
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    dst = cv2.warpPerspective(frame, M, (400, 600))
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Transformed Frame", dst)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
