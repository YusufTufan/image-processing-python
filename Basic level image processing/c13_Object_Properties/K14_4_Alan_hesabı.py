# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:17:17 2024

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

# İlk konturun alanını hesaplama
area = cv2.contourArea(contours[0])

# Alanı görüntünün sol üst köşesine ve konsola yazdırma
area_text = f'Area: {area}'
print(area_text)
cv2.putText(img, area_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Görüntüyü gösterme
cv2.imshow('Contour Area', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

