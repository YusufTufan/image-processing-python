# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:33:00 2024

@author: muozi
"""

import cv2
import numpy as np



img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)

cv2.line(img,(300,0),(300,459),(0,255,255),3)
cv2.imshow('cizgi',img)


cv2.waitKey(0)
cv2.destroyAllWindows()