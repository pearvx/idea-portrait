import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
window_name = "portrait0"
cv2.namedWindow(window_name)
vc = cv2.VideoCapture(0)
color = (51 , 255, 255)

width = vc.get(cv2.CAP_PROP_FRAME_WIDTH)
height = vc.get(cv2.CAP_PROP_FRAME_HEIGHT)

rval, frame = vc.read()
    
while True:

  if frame is not None:
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
     for (x, y, w, h) in faces:
         xmin = x
         xmax = xmin + w
         ypadding = int((h / 8))
         ymin = y - ypadding
         ymax = ymin + h + ypadding
         cv2.rectangle(frame, (xmin, ymin),(xmin + w, ymax), color, 2)

         xTextMin = xmin - 150
         xTextMax = xmax + 20
         textYPadding = 75
         if xTextMin > 0:
             birthdateY = ymin + 30
             cv2.putText(frame, "Birthdate", (xTextMin, birthdateY), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)
             genderY = birthdateY + textYPadding
             cv2.putText(frame, "Gender", (xTextMin, genderY), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)
             ageY = genderY + textYPadding
             cv2.putText(frame, "Age", (xTextMin, ageY), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)
         if xTextMax < width - 150:
             incomeY = ymin + 30
             cv2.putText(frame, "Income", (xTextMax, incomeY), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)
             phoneNumberY = incomeY + textYPadding
             cv2.putText(frame, "Phone Number", (xTextMax, phoneNumberY), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)
             heightY = phoneNumberY + textYPadding
             cv2.putText(frame, "Height", (xTextMax, ageY), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)
         # cv2.putText(frame, "Birthdate", (xTextMin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)
     cv2.imshow(window_name, frame)
  rval, frame = vc.read()

  if cv2.waitKey(1) & 0xFF == ord('q'):
     break

vc.release()
cv2.destroyAllWindows()

