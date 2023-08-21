# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 00:20:11 2023

@author: Harisudhan Ramaswamy
"""

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread(r"C:/Users/Harisudhan Ramaswamy/Pictures/i1Abv.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


height,width,channel = img.shape

#Show the output of each part

boxes = pytesseract.image_to_data(img)

print(boxes)
print(boxes.splitlines())


for x,b in enumerate(boxes.splitlines()):
    #Spliting at each space
    if x!= 0:
        b = b.split() 
        
        print(b)    
        if len(b) == 12:
            x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),1,cv2.LINE_4)
            cv2.putText(img,b[11],(x,y - 8),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)
        
    
cv2.imshow("RGB",img)
cv2.waitKey(0)