# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:08:46 2024

@author: muozi
"""

import numpy as np
import cv2

img = cv2.imread('R1_BUGDAY_TEK_renkli.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.blur(gray, (5, 5))
_, thresh = cv2.threshold(gray_blurred, 50, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Kontur bulma
contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(contours)
# Konturları çizme
img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

# Görüntüleri gösterme
cv2.imshow('Original Image', img)
cv2.imshow('Original Image gray', gray)
cv2.imshow('Original Image gray_blurred', gray_blurred)
cv2.imshow('Thresholded Image', thresh)
cv2.imshow('Contours', img_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()
