# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:07:24 2023

@author: Harisudhan Ramaswamy
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76


def get_img(img):
    image = cv2.imread(img)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def RGB2HEX(color):
    return "#(:02x)(:02x)(:02x)".format(int(color[0]), int(color[1]), int(color[2]))

def get_colors(image, no_cols, show_pie):
    modified_image = cv2.resize(image, (600,400), interpolation = cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], 3)
    
    clf = KMeans(n_clusters = no_cols)
    labels = clf.fit_predict(modified_image)
    counts = Counter(labels)
    center_colors = clf.cluster_centers_
    
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]
    

    fig = plt.figure(figsize = (10,10))
    plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)
    plt.show()
            
    return (rgb_colors)
    
print(get_colors(get_img("C:/Users/Harisudhan Ramaswamy/Pictures/earth-moon-minimalism-stars-wallpaper-preview.jpg"), 5, True))    
    
    
    
    
    
    
    
    
    
    
    
    
    