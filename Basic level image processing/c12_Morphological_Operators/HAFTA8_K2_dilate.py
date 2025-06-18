# -*- coding: utf-8 -*-
"""
Created on Fri May  5 10:34:02 2023

@author: MUOZIC
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
  
img = cv2.imread("yazi.jpg", 0)
  
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
  
kernel = np.ones((5, 5), np.uint8)
  
invert = cv2.bitwise_not(binr)
  
erosion = cv2.dilate(invert, kernel, iterations=2)
  
cv2.imshow("original",invert)
cv2.imshow("DİLATE",erosion)


cv2.waitKey(0)
cv2.destroyAllWindows()