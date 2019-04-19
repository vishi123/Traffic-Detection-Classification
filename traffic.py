import cv2
import numpy as np

cap=cv2.VideoCapture('videoplayback.mp4')

car_cascade=cv2.CascadeClassifier('cars.xml') 
font=cv2.FONT_HERSHEY_SIMPLEX

count=0


while True:
    ret, frame=cap.read()
    cv2.line(frame,(0,200),(1000,200),(255,0,0),3)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars=car_cascade.detectMultiScale(gray,1.1,3)
    
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        if (y+h)>200 and y<200:
            segment = "occupied"
            
        elif (y+h)>200 and y>200:
            if segment=="occupied":
               count+=1
               segment="released"
               

        cv2.putText(frame,"count: "+ str(count),(200,100),font,1,(0,255,0),2)
##            else:
##               return
##        roi_gray=gray[y:y+h, x:x+w]
##        roi_color=img[y:y+h, x:x+w]
        
##        for (ex,ey,ew,eh) in eyes:
##            cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        
    cv2.imshow('video',frame)

    k=cv2.waitKey(25) & 0xFF
    if k==27:
       break

    
cap.release()
cv2.destroyAllWindows()
