import numpy as np
import cv2

def titleAndSubtitle(title, subtitle, x, y):
    cv2.putText(frame, title, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)
    cv2.putText(frame, subtitle, (x, y + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)

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
             titleAndSubtitle("10/4/1973", "Birthdate", xTextMin, birthdateY)
             genderY = birthdateY + textYPadding
             titleAndSubtitle("Female", "Gender", xTextMin, genderY)
             ageY = genderY + textYPadding
             titleAndSubtitle("37", "Age", xTextMin, ageY)
         if xTextMax < width - 150:
             incomeY = ymin + 30
             titleAndSubtitle("$54,000", "Income", xTextMax, incomeY)
             phoneNumberY = incomeY + textYPadding
             titleAndSubtitle("312-229-9605", "Phone Number", xTextMax, phoneNumberY)
             heightY = phoneNumberY + textYPadding
             titleAndSubtitle("5' 86'", "Height", xTextMax, heightY)
         # cv2.putText(frame, "Birthdate", (xTextMin, ymin), cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)
     cv2.imshow(window_name, frame)
  rval, frame = vc.read()

  if cv2.waitKey(1) & 0xFF == ord('q'):
     break

vc.release()
cv2.destroyAllWindows()
