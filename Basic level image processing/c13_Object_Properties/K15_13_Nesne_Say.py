# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:37:39 2024

@author: muozi
"""


import numpy as np
import cv2

img = cv2.imread('img5_Bugday_Binary.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.blur(gray, (5, 5))
_, thresh = cv2.threshold(gray_blurred, 50, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Kontur bulma
contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Nesne sayısını al
object_count = len(contours)

# Konturları çizme ve nesne numaralarını yazdırma
img_contours = img.copy()
for i, contour in enumerate(contours):
    cv2.drawContours(img_contours, [contour], -1, (0, 255, 0), 2)
    # Ağırlık merkezini (centroid) bulma
    M = cv2.moments(contour)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    # Nesne numarasını yazdırma
    cv2.putText(img_contours, str(i+1), (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Nesne sayısını ekrana yazdır
print("Nesne Sayısı:", object_count)

# Görüntüleri gösterme
cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresh)
cv2.imshow('Contours', img_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()