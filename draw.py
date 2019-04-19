import numpy as np
import cv2

img = cv2.imread('flower.jpg', cv2.IMREAD_COLOR)
cv2.line(img, (0,0), (1000,0), (254,235,154),15)
cv2.rectangle(img,(15,25),(200,150),(0,255,134),5)
cv2.circle(img, (100,63),25,(134,134,134),4)
pts = np.array([ [10,15], [20,15], [10,30],[20,30] ], np.int32)
##pts = pts.reshape((-1,1,2))

cv2.polylines(img, [pts], True ,(134,234,215),5)

#to write on image
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img ,'hope all will go well',(0,130),font,1,(200,255,255),2,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

