# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 00:06:57 2019

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
import csv



image = imread('ImageRequete.jpg')
feature_matrix = np.zeros((660,450)) 
feature_matrix.shape
imshow(image)

output = open("index.csv", "w")
for i in range(0,image.shape[0]):
    for j in range(0,image.shape[1]):
        feature_matrix[i][j] = ( (int(image[i,j,0]) + int(image[i,j,1]) + int(image[i,j,2]))/3)
        print(feature_matrix[i][j])
        
        
A = np.squeeze(np.asarray(feature_matrix))
with open('people.csv', 'w') as writeFile:
    writer = csv.writer(feature_matrix[i][j])
    writer.writerows(feature_matrix[i][j])

writeFile.close()
        
