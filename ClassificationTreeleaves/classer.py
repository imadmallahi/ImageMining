# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 18:12:36 2020

@author: pc
"""
import os
from ReliefF import ReliefF
import numpy as np
import pandas as pd
import csv
from sklearn import svm
from Features import ColorDescriptor
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pickle
from sklearn.decomposition import PCA
import glob
import cv2

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier


X_train = pickle.load(open('C:/Users/pc/Desktop/exam_midvi/serial_X', 'rb'))
Y_train = pickle.load(open('C:/Users/pc/Desktop/exam_midvi/serial_Y', 'rb'))

X_train2=[]
for l in X_train:
    ll=eval(l)
    X_train2.append(ll)
    
X_train=np.asarray(X_train2)
Y_train=np.asarray(Y_train)

#cl=svm.SVC(kernel="rbf",gamma=0.1)
#cl=svm.SVC()
#cl = KNeighborsClassifier(n_neighbors=8, metric='euclidean')
#cl = GaussianNB()
#cl = tree.DecisionTreeClassifier()
cl = RandomForestClassifier(max_depth=8, random_state=0)
cl.fit(X_train,Y_train)




liste=[]
x_test=[]
y_test=[]
cd = ColorDescriptor((8, 12, 3))

for element in os.listdir('C:/Users/pc/Desktop/exam_midvi/PlantDiseaseDataSet/validation'):    
    a=glob.glob('C:/Users/pc/Desktop/exam_midvi/PlantDiseaseDataSet/validation/'+element+'/*.jpg')
    
    for f in a:    
        image=cv2.imread(f)
        features = cd.describe(image)
        liste.append({'classe':element ,'path': f , 'v':features})
    
en_tetes = ['classe','path', 'v']
with open('C:/Users/pc/Desktop/exam_midvi/test.csv','w', newline='') as ff:
    f_csv = csv.DictWriter(ff, en_tetes)
    f_csv.writeheader()
    f_csv.writerows(liste)
    
    
data=pd.read_csv('C:/Users/pc/Desktop/exam_midvi/test.csv')

X_test = data.drop('classe',1) 
X_test = X_test.drop('path',1)
X_test = data["v"]
Y_test = data["classe"]
names = data["path"]


X_test2=[]
for l in X_test:
    ll=eval(l)
    X_test2.append(ll)

X_test=np.asarray(X_test2)
Y_test=np.asarray(Y_test)

for v,name in zip(X_test, names):
    img = mpimg.imread(name)
    plt.imshow(img)
    print(cl.predict(v.reshape(1,-1)))
    plt.show()
    
Y_pred=cl.predict(X_test)
score=cl.score(X_test, Y_test)
cm=confusion_matrix(Y_test, Y_pred)