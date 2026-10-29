import sys, os
try:
    import cv2
except ModuleNotFoundError:
    _py = r"C:\Users\habee\AppData\Local\Programs\Python\Python313\python.exe"
    if os.path.exists(_py) and os.path.abspath(sys.executable).lower() != os.path.abspath(_py).lower():
        os.execv(_py, [_py] + sys.argv)
    raise
import cv2

# NOTE: needs a video file. Download demonslayer.mp4 and set path below.
cap = cv2.VideoCapture("C:\\Users\\habee\\OpenCV\\demonslayer.mp4")
slow_factor = 0.5
fast_factor = 2.0
ret, frame = cap.read()
while ret:
    cv2.imshow('Slow Motion', cv2.resize(frame, None, fx=slow_factor, fy=slow_factor))
    cv2.imshow('Fast Motion', cv2.resize(frame, None, fx=fast_factor, fy=fast_factor))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    ret, frame = cap.read()
cap.release()
cv2.destroyAllWindows()
