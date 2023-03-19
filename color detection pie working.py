# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:44:36 2023

@author: Harisudhan Ramaswamy
"""
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import io
from tkinter.filedialog import askopenfilename

# Loading the image with a pop up; 
img = Image.open(askopenfilename())

#and converting it to RGB format
img.convert('RGB')

# Getting the colors in the image as a array(flattened) of RGB tuples
colors = np.array(img.getdata())
colors = colors.reshape((-1, 3))

# Convert RGB tuples to hex color codes
hex_colors = ['#%02x%02x%02x' % tuple(c) for c in colors]

# Count the occurrences of each color code
color_counts = dict()
for hex_code in hex_colors:
    if hex_code in color_counts:
        color_counts[hex_code] += 1
    else:
        color_counts[hex_code] = 1

# Create a pie chart of the color distribution
labels = list(color_counts.keys())
counts = list(color_counts.values())
plt.pie(counts, labels=labels, colors=labels)
plt.show()