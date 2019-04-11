import numpy as np
import cv2
from button import button_pressed

COLOR = (22 , 231, 248)
WINDOW_NAME = "portrait0"
MODEL_PATH = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(MODEL_PATH)
video_capture = cv2.VideoCapture(0)
window_width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)

def init():
    cv2.namedWindow(WINDOW_NAME)

def titleAndSubtitle(frame, title, subtitle, x, y):
    cv2.putText(frame, title, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, COLOR, 2)
    cv2.putText(frame, subtitle, (x, y + 25), cv2.FONT_HERSHEY_SIMPLEX, 0.45, COLOR, 2)

def runPortrait():
    rval, frame = video_capture.read()

    while True:

      if frame is not None:
         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
         faces = face_cascade.detectMultiScale(gray, 1.3, 5)
         for (x, y, w, h) in faces:

             # Draw box around face
             xmin = x
             xmax = xmin + w
             ypadding = int((h / 8))
             ymin = y - ypadding
             ymax = ymin + h + ypadding
             cv2.rectangle(frame, (xmin, ymin),(xmin + w, ymax), COLOR, 2)

             # Calculate and add each text box around rectangle
             xTextMin = xmin - 150
             xTextMax = xmax + 20
             textYPadding = 75
             if xTextMin > 0:
                 birthdateY = ymin + 30
                 titleAndSubtitle(frame, "10/4/1973", "Birthdate", xTextMin, birthdateY)
                 genderY = birthdateY + textYPadding
                 titleAndSubtitle(frame, "Female", "Gender", xTextMin, genderY)
                 ageY = genderY + textYPadding
                 titleAndSubtitle(frame, "37", "Age", xTextMin, ageY)
             if xTextMax < window_width - 150:
                 incomeY = ymin + 30
                 titleAndSubtitle(frame, "$54,000", "Income", xTextMax, incomeY)
                 phoneNumberY = incomeY + textYPadding
                 titleAndSubtitle(frame, "312-229-9605", "Phone Number", xTextMax, phoneNumberY)
                 heightY = phoneNumberY + textYPadding
                 titleAndSubtitle(frame, "5' 86'", "Height", xTextMax, heightY)
         cv2.imshow(WINDOW_NAME, frame)
      rval, frame = video_capture.read()

      if cv2.waitKey(1) & 0xFF == ord('q'):
         break

    video_capture.release()
    cv2.destroyAllWindows()

init()
runPortrait()
