# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 18:22:41 2019

@author: pc
"""

import numpy as np
import cv2
import imutils
 
class ColorDescriptor:
	def __init__(self, bins):
		self.bins = bins
 
	def describe(self, image):
		# convertire l image de RVB ====> HSV
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		vectDescripteur = []
 
		# calculer le centre d'image
		(h, w) = image.shape[:2]
		(cX, cY) = (int(w * 0.5), int(h * 0.5))
        
        #diviser l'image en 4 rectangle 
		segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),
			(0, cX, cY, h)]
        
		# boucler sur le segment
		for (startX, endX, startY, endY) in segments:
			# construire un masque pour chaque coin de l'image
			cornerMask = np.zeros(image.shape[:2], dtype = "uint8")
			cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
 
            #extraire l'histogramme d'image et modifier le vecteur descripteur
			hist = self.histogram(image, cornerMask)
			vectDescripteur.extend(hist)

 
		# retourner le vecteur descripteur 
		return vectDescripteur

	def histogram(self, image, mask):
        #extraire l'histogramme 3D de la region masqué d'image 
		hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,
			[0, 255, 0, 256, 0, 256])
 
		#normalizer l'histogramme si la version de openCV est OpenCV 2.4
		if imutils.is_cv2():
			hist = cv2.normalize(hist).flatten()
 
		#normalizer l'histogramme si la version de openCV est 3+
		else:
			hist = cv2.normalize(hist, hist).flatten()
 
		# retourner l'histogramme
		return hist