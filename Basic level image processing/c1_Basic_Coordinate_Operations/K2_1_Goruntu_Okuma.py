# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 22:54:19 2024

@author: muozi
"""

import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)

cv2.waitKey(10000)
cv2.destroyAllWindows()