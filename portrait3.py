import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
window_name = "portrait3"
cv2.namedWindow(window_name)
vc = cv2.VideoCapture(0)
color = (0, 255, 0)

width = vc.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
height = vc.get(cv2.CAP_PROP_FRAME_HEIGHT)

rval, frame = vc.read()

mask = np.ones(frame.shape, dtype=np.uint8)
    
while True:

  if frame is not None:
     # cv2.fillPoly(frame, roi_corners, color)
     # cv2.GaussianBlur(frame(xmin), frame(roi_corners), (0, 0), 4)
     mask.fill(0)
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
     for (x, y, w, h) in faces:
         xmin = width - x - 40
         xmax = xmin + 40
         ymin = y
         ymax = ymin + 40
         roi_corners = np.array([[(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]], dtype=np.int32)
         cv2.fillPoly(mask, roi_corners, color)
         # cv2.rectangle(frame, (x, y),(x+w, y+h),(255, 0, 0), 2)
     cv2.imshow(window_name, mask)
  rval, frame = vc.read()

  if cv2.waitKey(1) & 0xFF == ord('q'):
     break

vc.release()
cv2.destroyAllWindows()
