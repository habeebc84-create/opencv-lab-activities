import sys, os
try:
    import cv2
except ModuleNotFoundError:
    _py = r"C:\Users\habee\AppData\Local\Programs\Python\Python313\python.exe"
    if os.path.exists(_py) and os.path.abspath(sys.executable).lower() != os.path.abspath(_py).lower():
        os.execv(_py, [_py] + sys.argv)
    raise
import cv2

# NOTE: needs demonslayer.mp4. Download and place in OpenCV folder.
cap = cv2.VideoCapture("C:\\Users\\habee\\OpenCV\\demonslayer.mp4")
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
for i in reversed(range(num_frames)):
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Reverse Video', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
