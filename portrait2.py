import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
window_name = "portrait2"
cv2.namedWindow(window_name)
vc = cv2.VideoCapture(0)
color = (255 , 0, 153)

width = vc.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
height = vc.get(cv2.CAP_PROP_FRAME_HEIGHT)

rval, frame = vc.read()
    
while True:

  if frame is not None:
     # cv2.fillPoly(frame, roi_corners, color)
     # cv2.GaussianBlur(frame(xmin), frame(roi_corners), (0, 0), 4)
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
     for (x, y, w, h) in faces:
         xmin = x
         xmax = x + w
         ymin = y
         ymax = y + h
         roi_corners = np.array([[(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]], dtype=np.int32)
         cv2.fillPoly(frame, roi_corners, color)
         # cv2.rectangle(frame, (x, y),(x+w, y+h),(255, 0, 0), 2)
     cv2.imshow(window_name, frame)
  rval, frame = vc.read()

  if cv2.waitKey(1) & 0xFF == ord('q'):
     break

vc.release()
cv2.destroyAllWindows()

