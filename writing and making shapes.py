import numpy as np
import cv2

img = cv2.imread('akku.jpg',cv2.IMREAD_COLOR)

#cv2.line(img,(0,160),(243,160),(0,0,0),5)
cv2.rectangle(img,(80,50),(150,160),(0,0,255),2)
cv2.circle(img,(115,105), 50, (0,255,0), 1)
pts = np.array([[70,105],[100,40],[160,40],[160,150],[80,160]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Akku',(10,20), font, 1, (0,5,5), 3, cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
