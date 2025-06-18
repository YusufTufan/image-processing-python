# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 09:21:45 2024

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

# En küçük çevreleyen çemberin merkezini ve yarıçapını bulma
(l, k), radius = cv2.minEnclosingCircle(contours[0])
center = (int(l), int(k))
radius = int(radius)

# En küçük çevreleyen çembreyi çizme
img_circle = img.copy()
cv2.circle(img_circle, center, radius, (0, 255, 0), 2)
cv2.circle(img_circle, center, 5, (0, 255, 255), 3)
cv2.line(img_circle, center, (center[0], center[1]+radius), (0, 0, 255), 2)
cv2.line(img_circle, center, (center[0], center[1]-radius), (0, 0, 255), 2)
cv2.line(img_circle, center, (center[0]+radius, center[1]), (0, 0, 255), 2)
cv2.line(img_circle, center, (center[0]-radius, center[1]), (0, 0, 255), 2)

# Merkez ve yarıçap bilgilerini yazdırma
cv2.putText(img_circle, f"Center: ({center[0]}, {center[1]})", (center[0] - 50, center[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
cv2.putText(img_circle, f"Radius: {radius}", (center[0] - 50, center[1] + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# Görüntüyü gösterme
cv2.imshow('Minimum Enclosing Circle', img_circle)

cv2.waitKey(0)
cv2.destroyAllWindows()

