# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 23:35:05 2023

@author: MUOZIC
"""


#Import the necessary libraries
import cv2
import matplotlib.pyplot as plt
import numpy as np
  

img = cv2.imread('Resim18_Bitewing2.jpg')
  
  
# Create the sharpening kernel
kernel = np.array([[0, -1, 0], [-1, 6, -1], [0, -1, 0]])
  
# Sharpen the image
sharpened_image = cv2.filter2D(img, -1, kernel)
  

  
cv2.imshow("original",img)
cv2.imshow("sharpened_image",sharpened_image)


cv2.waitKey(0)
cv2.destroyAllWindows()