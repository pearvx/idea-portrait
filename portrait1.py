import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
window_name = "portrait2"
cv2.namedWindow(window_name)
vc = cv2.VideoCapture(0)
color = (51 , 255, 255)

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
         xmax = xmin + w
         ypadding = int((h / 8))
         ymin = y - ypadding
         ymax = ymin + h
         bodyYmax = int(height)
         bodyXmin = x - w
         face_img = frame[ymin:y+h+ypadding, x:x+w]
         body_img = frame[ymax:bodyYmax, bodyXmin:x+w+w]
         blurred_face_img = cv2.GaussianBlur(face_img,(53, 53), 100)
         blurred_body_img = cv2.GaussianBlur(body_img,(53, 53), 100)
         if blurred_face_img is not None:
             frame[ymin:ymin + blurred_face_img.shape[0], x:x+blurred_face_img.shape[1]] = blurred_face_img
         if blurred_body_img is not None:
             frame[ymax:ymax + blurred_body_img.shape[0], bodyXmin:bodyXmin+blurred_body_img.shape[1]] = blurred_body_img
     cv2.imshow(window_name, frame)
  rval, frame = vc.read()

  if cv2.waitKey(1) & 0xFF == ord('q'):
     break

vc.release()
cv2.destroyAllWindows()

