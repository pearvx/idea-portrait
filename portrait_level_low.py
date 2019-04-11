import numpy as np
import cv2

COLOR = (238, 238, 34)
WINDOW_NAME = "portrait3"
MODEL_PATH = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(MODEL_PATH)
video_capture = cv2.VideoCapture(0)
window_width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)

def init():
    cv2.namedWindow(WINDOW_NAME)
    
def title(frame, title, x, y):
    cv2.putText(frame, title, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.75, COLOR, 2)

def runPortrait():
    rval, frame = video_capture.read()

    mask = np.ones(frame.shape, dtype=np.uint8)
        
    while True:

      if frame is not None:
         mask.fill(0)
         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         faces = face_cascade.detectMultiScale(gray, 1.3, 5)
         for (x, y, w, h) in faces:
             xmin = window_width - x - 40
             xmax = xmin + 40
             ymin = y
             ymax = ymin + 40
             xTextMin = xmin - 15
             title(mask, "Human", xTextMin, ymin - 30)
             roi_corners = np.array([[(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]], dtype=np.int32)
             cv2.fillPoly(mask, roi_corners, COLOR)
         cv2.imshow(WINDOW_NAME, mask)
      rval, frame = video_capture.read()

      if cv2.waitKey(1) & 0xFF == ord('q'):
         break

    video_capture.release()
    cv2.destroyAllWindows()

init()
runPortrait()
