# CBIR : Content Based Image Retreivial
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import color
from skimage.feature.texture import greycoprops,greycomatrix


def show_img(path,i,title):
	"""
	path : path to image that we will show
	i    : index of subplot
	title: title of the subplot
	"""
	img = cv2.imread(path)
	plt.subplot(2, 3, i)
	plt.axis("off")
	plt.title(title)
	plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


def hsvHistogramFeatures(img):
	rows, cols, numOfBands = img.shape[:]
	img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
	h = img[:,:,0]
	s = img[:,:,1]
	v = img[:,:,2]
	numberOfLevelsForH = 8 
	numberOfLevelsForS = 2 
	numberOfLevelsForV = 2 
	maxValueForH = np.max(h)
	maxValueForS = np.max(s)
	maxValueForV = np.max(v)
	hsvColor_Histogram = np.zeros((8, 2, 2))
	quantizedValueForH = np.ceil( h.dot(numberOfLevelsForH) / maxValueForH)
	quantizedValueForS = np.ceil( s.dot(numberOfLevelsForS) / maxValueForS)
	quantizedValueForV = np.ceil( v.dot(numberOfLevelsForV) / maxValueForV)
	index = np.zeros((rows*cols, 3))
	#print(quantizedValueForH.shape[0] * quantizedValueForH.shape[1])
	index[:,0] = quantizedValueForH.reshape(1,-1).reshape(1,quantizedValueForH.shape[0] * quantizedValueForH.shape[1]) 
	index[:,1] = quantizedValueForS.reshape(1,-1).reshape(1,quantizedValueForS.shape[0] * quantizedValueForS.shape[1]) 
	index[:,2] = quantizedValueForV.reshape(1,-1).reshape(1,quantizedValueForV.shape[0] * quantizedValueForV.shape[1])
	k=0
	for row in range(len(index[:,0])):
		if index[row,0] == 0 or index[row,1] == 0 or index[row,2] == 0:
			k+=1
			continue
		hsvColor_Histogram[int(index[row,0])-1,int(index[row,1])-1,int(index[row,2])-1] = hsvColor_Histogram[int(index[row,0])-1,int(index[row,1])-1,int(index[row,2])-1] + 1
	#print(k,index[:,0].shape)
	hsvColor_Histogram = hsvColor_Histogram[:].reshape(1,-1)
	hsvColor_Histogram = hsvColor_Histogram/np.sum(hsvColor_Histogram)
	return hsvColor_Histogram.reshape(-1)

def extractColorFeature(img):
	R = img[:,:,0]
	G = img[:,:,1]
	B = img[:,:,2]
	features = [np.mean(R),np.std(R),np.mean(G),np.std(G),np.mean(B),np.std(B)]
	features/=np.mean(features)
	return features

def textureFeatures(img):
	img = color.rgb2gray(img)
	img = skimage.img_as_ubyte(img)
	glcm = greycomatrix(img, [1], [0], 256, symmetric=True, normed=True)
	feature = greycoprops(glcm, 'dissimilarity')[0]
	feature = np.concatenate([feature,greycoprops(glcm, 'correlation')[0]])
	feature = np.concatenate([feature,greycoprops(glcm, 'contrast')[0]])
	feature = np.concatenate([feature,greycoprops(glcm, 'energy')[0]])
	feature = feature/np.sum(feature)
	#print(feature)
	return feature

def shapeFeatures(img):
	img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	_,img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
	feature = cv2.HuMoments(cv2.moments(img))
	return feature.reshape(-1)

def getFeatures(img,featuresSize):
	if featuresSize >= 7 :
		features = extractColorFeature(img)
	if featuresSize >= 39 :
		features = np.concatenate([features, hsvHistogramFeatures(img)])
	if featuresSize >= 43:
		features = np.concatenate([features, textureFeatures(img)])
	if featuresSize >= 50:
		features = np.concatenate([features, shapeFeatures(img)])
	#print(features)
	return features


def extractAllFeatures(files,fsize,mode = 1):
	if mode == 1:
		v = []
		for f in files:
			img = cv2.imread(f)
			v.append(getFeatures(cv2.cvtColor(img, cv2.COLOR_BGR2RGB),fsize))	
		np.save('features.npy',v,allow_pickle=True)
	else :
		v = np.load('features.npy',allow_pickle=True)
	return v
def CBIR_Search(features, image_req,fsize):
	feature_req = getFeatures(image_req,fsize)
	dist = []
	for feature in features:
		dist.append(euclidien_distance(feature,feature_req))
	dist = np.argsort(dist)[:5].tolist()
	return dist

def euclidien_distance(A,B):
	dist = (A - B)**2
	dist = np.sum(dist,axis = 0)
	return np.sqrt(dist)

def main():
    '''
	images_path = '../../Atelier_1/obj_decoys'
	fsize = 50
	files = [os.path.join(images_path,p) for p in sorted(os.listdir(images_path))]
	features = extractAllFeatures(files,fsize,1) # 0 if you already have the features.npy(second time to run the code) , 1 id the first time you run this code
	image_req_path = '../../Atelier_1/ImageRequete.jpg'
	image_req = cv2.cvtColor(cv2.imread(image_req_path), cv2.COLOR_BGR2RGB)
	dist = CBIR_Search(features,image_req,fsize)
	show_img(image_req_path,1,'Request Image')
	for i in range(5):
		show_img(files[dist[i]],i+2,'Result Image '+ str(i+1))
	plt.show()
'''
if __name__ == '__main__':
	main()



