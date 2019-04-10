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
     mask.fill(0)
     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
     box_width = 40
     box_height = 40
     padding = 30
     num_of_width = 5
     num_of_height = 5
     topLevelArray = np.array([])
     originX = 10
     originY = 10
     previousYMax = originY
     for i in range(num_of_height):
         subLevelArray = np.array([])
         previousMax = originX
         ymin = previousYMax
         ymax = ymin + box_height
         for j in range(num_of_width):
             xmin = previousMax
             xmax = xmin + box_width
             
             np.append(subLevelArray, [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)])
             previousMax = xmax + padding
         np.append(topLevelArray, subLevelArray)
         previousYMax = ymax + padding
     cv2.fillPoly(mask, topLevelArray, color)
     cv2.imshow(window_name, mask)
  rval, frame = vc.read()

  if cv2.waitKey(1) & 0xFF == ord('q'):
     break

vc.release()
cv2.destroyAllWindows()

