# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 09:54:50 2024

@author: muozi
"""

import numpy as np
import cv2

img = cv2.imread('R1_BUGDAY_TEK_renkli.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.blur(gray, (5, 5))
_, thresh = cv2.threshold(gray_blurred, 50, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

x, y, w, h = cv2.boundingRect(contours[0])
aspect_ratio = round(w / h, 2)

img_contours = img.copy()
cv2.putText(img_contours, f'Aspect Ratio: {aspect_ratio}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresh)
cv2.imshow('Contours with Aspect Ratio', img_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()
