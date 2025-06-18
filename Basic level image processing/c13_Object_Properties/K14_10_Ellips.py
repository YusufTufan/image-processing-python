# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:14:31 2024

@author: muozi
"""

import numpy as np
import cv2

img = cv2.imread('R1_BUGDAY_TEK_renkli.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.blur(gray, (5, 5))
_, thresh = cv2.threshold(gray_blurred, 50, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Elips fit etme
ellipse = cv2.fitEllipse(contours[0])

# Görüntüye çizim
img_contours = img.copy()
cv2.ellipse(img_contours, ellipse, (0, 255, 255), 2)  # Elipsi çiz

cv2.imshow('Elips Visualization', img_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()
