# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:57:01 2019

@author: user
"""
from pyimagesearch.colordescriptor import ColorDescriptor
import pandas as pd

import numpy as np
import csv
import cv2
import glob
import matplotlib.pyplot as plt
from skimage.io import imread, imshow

image = imread('ImageRequete.jpg', as_gray=True)
imshow(image)

# initialize the color descriptor
cd = ColorDescriptor((8, 12, 3))

print("la taile image ",image.size)
print("shape img",image.shape)

#checking image shape 
image.shape, image
features = np.reshape(image, (80*120))

features.shape, features
print ("vector shape",features)
print("feature shape",features.shape)

T=[]
output = open("mellahi12.csv", "w+")

for imagePath in glob.glob("DataSet" + "/*.jpg"):
    # extract the image ID (i.e. the unique filename) from the image
	# path and load the image itself
	T.append( imagePath[imagePath.rfind("/")+1: ])


for i in T:
    
    image = imread(i, as_gray=True)
    imshow(image)
    #checking image shape 
    image.shape, image
    features = cd.describe(image)
    print ("vector shape",features)
    print("feature shape",features.shape)
    values = ','.join(str(v) for v in features)
    output.write("%s : %s \n"%( i,values))
    

output.close()
        


    
   
    