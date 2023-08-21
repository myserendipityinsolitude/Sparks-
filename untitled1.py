# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 09:06:59 2023

@author: Harisudhan Ramaswamy
"""

import cv2
from matplotlib import colors
import numpy as np
import os 
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

from collections import Counter

from skimage.color import rgb2lab

def RGB2HEX (color):
    return "#{:02x} {:02x} {:02x}". format(int(color[0]), int(color[1]), int(color[2]))

def get_image (image_path) :
    image=cv2.imread (image_path)
    image=cv2.cvtColor (image, cv2.COLOR_BGR2RGB)
    return image

def get_colors(image, number_of_colors, show_chart):
    modified_im = cv2.resize (image, (600,400), interpolation = cv2.INTER_AREA)
    modified_im = modified_im.reshape (modified_im.shape[0]*modified_im.shape[1],3)

    clf= KMeans(n_clusters = number_of_colors)
    labels = clf.fit_predict(modified_im)

    counts = Counter (labels)
    center_colors = clf.cluster_centers_

    ordered_colors=[center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i])for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    if (show_chart):
        fig=plt.figure(figsize = (8,6))
        plt.pie(counts.values(), labels=hex_colors,colors=hex_colors)
        plt.show()
    return rgb_colors
print(get_colors(get_image(r"C:/Users/Harisudhan Ramaswamy/Pictures/836375.webp"), 5, True))