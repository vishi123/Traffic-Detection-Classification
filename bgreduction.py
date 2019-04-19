import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import logging
import logging.handlers
import random


##def get_centroid(x, y, w, h):
##    x1 = int(w / 2)
##    y1 = int(h / 2)
##
##    cx = x + x1
##    cy = y + y1
##
##    return (cx, cy)

cap=cv2.VideoCapture('traffic1.mp4')
fgbg=cv2.createBackgroundSubtractorMOG2()
##car_cascade=cv2.CascadeClassifier('cars.xml') 
font=cv2.FONT_HERSHEY_SIMPLEX
segment="released"
count=0

while True:
    ret, frame=cap.read()
    fgmask=fgbg.apply(frame)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    fgmask=cv2.medianBlur(fgmask,15)
    fgmask=cv2.threshold(fgmask,240,255,cv2.THRESH_BINARY) [1]
    
    kernel=np.ones((5,5),np.uint8)
    edges=cv2.erode(fgmask,kernel,iterations=2)
    edges=cv2.dilate(fgmask,kernel,iterations=2)
    
##    opening=cv2.morphologyEx(fgmask,cv2.MORPH_OPEN, kernel)
##    closing=cv2.morphologyEx(fgmask,cv2.MORPH_CLOSE, kernel)
    cv2.line(frame,(0,250),(1000,250),(255,0,0),3)
    
    blurred= cv2.GaussianBlur(fgmask, (7, 7), 0)
    edges = cv2.Canny(blurred,100,200)
##    

##                         return matches
    (_,cnts,_)=cv2.findContours(edges.copy(),cv2.RETR_EXTERNAL,  cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        if y==250:
            segment = "occupied"
            count+=1
            
##        elif (y+h)>200 and y>200:
##            if segment=="occupied":
##               count+=1
            segment="released"
               

        cv2.putText(frame,"count: "+ str(count),(200,100),font,1,(0,255,0),2)
##    

    cv2.imshow('original',frame)
    cv2.imshow('fg' ,fgmask)

    k=cv2.waitKey(30) & 0xFF
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
