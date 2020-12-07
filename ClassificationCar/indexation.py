# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 18:58:19 2019

@author: pc
"""

import glob
import csv
from getFeatures import ColorDescriptor
import cv2
import os
from scipy import stats

path='DB2C'
files = []
liste=[]
a=glob.glob('DB2C/obj_car/*.jpg')
cd = ColorDescriptor((8, 12, 3)) 


    
for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:            
            files.append(os.path.join(r, file))
        
cd = ColorDescriptor((8, 12, 3)) 
    
for f in files:    
    c_=f.split('\\')
    class_=c_[1].split('_')   
    image=cv2.imread(f)
    features = cd.describe(image)
    print
    liste.append({'class': class_[1] , 'v':features})



en_tetes = ['class', 'v']
with open('DB2C/obj1.csv','w+', newline='') as ff:
    f_csv = csv.DictWriter(ff, en_tetes)
    #f_csv.writeheader()
    f_csv.writerows(liste)
    

    

