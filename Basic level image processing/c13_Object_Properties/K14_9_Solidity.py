# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:06:03 2024

@author: muozi
"""

import numpy as np
import cv2

img = cv2.imread('R1_BUGDAY_TEK_renkli.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.blur(gray, (5, 5))
_, thresh = cv2.threshold(gray_blurred, 50, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour_area = cv2.contourArea(contours[0])
hull = cv2.convexHull(contours[0])
hull_area = cv2.contourArea(hull)
solidity = round(contour_area / hull_area, 2)

img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)  # Konturu çiz
cv2.drawContours(img_contours, [hull], -1, (255, 0, 0), 2)  # Konveks gövdeyi çiz
cv2.putText(img_contours, f'Solidity: {solidity}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv2.imshow('Solidity Visualization', img_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()
