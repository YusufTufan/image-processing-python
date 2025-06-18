# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:17:56 2024

@author: muozi
"""

import numpy as np
import cv2

# Görüntüyü oku
img = cv2.imread('R1_BUGDAY_TEK_renkli.png')

# Gri tonlamaya çevir ve eşikleme yap
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.blur(gray, (5, 5))
_, thresh = cv2.threshold(gray_blurred, 50, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Konturları bul
contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Elipsi fit et
ellipse = cv2.fitEllipse(contours[0])
(xc, yc), (major_axis, minor_axis), angle = ellipse

# Eksantriklik hesapla
if major_axis > minor_axis:
    a = major_axis / 2  # Major eksenin yarısı
    b = minor_axis / 2  # Minor eksenin yarısı
else:
    a = minor_axis / 2
    b = major_axis / 2

eccentricity = round(np.sqrt(1 - (b ** 2 / a ** 2)), 2)

# Elipsi çiz ve eksantriklik değerini yazdır
img_contours = img.copy()
cv2.ellipse(img_contours, ellipse, (0, 255, 255), 2)  # Elipsi çiz
cv2.putText(img_contours, f'Eccentricity: {eccentricity}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Görüntüyü göster
cv2.imshow('Eccentricity and Ellipse Visualization', img_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()

