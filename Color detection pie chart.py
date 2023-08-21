# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 15:33:25 2023

@author: Harisudhan Ramaswamy
"""

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Load
img = Image.open("C:/Users/Harisudhan Ramaswamy/Pictures/wallpaper.png")

# Image is converted into a numpy array
img_arr = np.array(img)

# Flattening the array and getting the unique colors
colors, counts = np.unique(img_arr.reshape(-1, img_arr.shape[-1]), axis=0, return_counts=True)

# Converting the colors to hex format
colors_hex = ['#' + ''.join([f'{c:02X}' for c in color]) for color in colors]

# Plotting the pie chart
plt.pie(counts, labels=colors_hex, colors=colors_hex, radius = )
plt.axis('equal')
plt.show()