# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 10:32:31 2023

@author: Harisudhan Ramaswamy
"""
import cv2
import numpy as np
import time


# recording from camera (input)
vid = cv2.VideoCapture(0)
  
timeout = time.time() + 60*1   # 1 minute from now
    
# loop runs for given time (ie) 1 min

while True:
    test = 0
    # capturing the current frame
    _, frame = vid.read()
  
    # displaying the current frame
    cv2.imshow("frame", frame) 
  
    # setting values for base colors
    b = frame[:, :, :1]
    g = frame[:, :, 1:2]
    r = frame[:, :, 2:]
  
    # computing the mean
    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)
  
    # here i shall only display the most prominent color in the frame
    if (b_mean > g_mean and b_mean > r_mean):
        print("Blue")
    if (g_mean > r_mean and g_mean > b_mean):
        print("Green")
    else:
        print("Red")
        
    if test == 1 or time.time() > timeout:
        print("Program ended....")
        break
    test = test - 1    