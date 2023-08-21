# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:07:56 2023

@author: Harisudhan Ramaswamy
"""

import cv2
import numpy as np  
  
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,3000)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,2400)
  
while(True):  
    # Capture image frame-by-frame  
    ret, frame = cap.read()  
    height,width,_ = frame.shape
    cx = (width//2)
    cy = (height//2)
    text = "RED"
    #pick pixel value
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    pixel_cen = hsv[cy,cx]
    BGR_img = frame[cy,cx]
    b,g,r = int(BGR_img[0]),int(BGR_img[1]),int(BGR_img[2])
    print()
    cv2.circle(frame,(cx,cy),5,(255,0,0),3)
    if(pixel_cen[0]<5):
        text = "RED"
    elif(pixel_cen[0]<22):
        text = "ORANGE"
    elif(pixel_cen[0]<33):
        text = "YELLOW"
    elif(pixel_cen[0]<78):
        text = "GREEN"
    elif(pixel_cen[0]<131):
        text = "BLUE"
    # Our operations on the frame come here  
    frame = cv2.rectangle(frame, (0,10), (250,60), (0,0,0), -1)
    frame = cv2.putText(frame,text,(50, 50),cv2.FONT_HERSHEY_SIMPLEX,1,(b,g,r),2,cv2.LINE_AA)
    # Display the resulting frame  
    cv2.imshow('frame',frame)  
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  
  
cap.release()  
cv2.destroyAllWindows()