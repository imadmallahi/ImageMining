# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:40:53 2019

@author: pc
"""

import csv
from sklearn import svm
from  getFeatures import ColorDescriptor
import cv2
import glob
import imageio
import matplotlib.pyplot as plt


X=[]
Y=[]
with open("DB2C/obj.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                for vectDescripteur in row[1:]:                     
                    vectDescripteur=eval(vectDescripteur)
#                   results[row[0]] = d
                    X.append(vectDescripteur)
                    print(row[0])
                    if row[0]=='car':
                        Y.append("car")
                    else:
                        Y.append("ship")
            f.close()
            

cl=svm.LinearSVC()
#X=[[1,0],[0,1],[0,0],[1,1]]
#Y=[0,0,0,1]
cl.fit(X,Y)

a=glob.glob('DataToPredict/*.jpg')
cd = ColorDescriptor((8, 12, 3))
restltat=[]
for f in a:
    image=cv2.imread(f)
    features = cd.describe(image)
    print(f, cl.predict([features]))
    restltat.append({'image':f,'predict':cl.predict([features])})
    img = imageio.imread(f)
    plt.imshow(img)
    plt.show()
    
for row in restltat:
    print(row['image'].split('\\')[1])
    print(row['predict'])
    

csv_filename = 'Prediction_Atelier2_corelDB_Imade.csv'
with open(csv_filename, 'a', newline='') as csvfile:
    fieldnames = ['Name', 'Classe']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()        
    for row in restltat:
            filename = row['image'].split('\\')[1]
            classname = row['predict']
            writer.writerow({'Name' : filename, 'Classe' : classname})

