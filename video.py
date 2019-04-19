import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')#for making video
out = cv2.VideoWriter('output.mkv' , fourcc, 20.0, (640,480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame' ,frame)
    cv2.imshow('gray' , gray)

    if cv2.waitKey(1) & 0xFF == ord('m'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()
