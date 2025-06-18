
"""
Created on Tue Apr 16 09:35:23 2024

@author: muozi
"""

import numpy as np
import cv2

img = cv2.imread('img5_Bugday_Binary.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.blur(gray, (5, 5))
_, thresh = cv2.threshold(gray_blurred, 50, 255, cv2.THRESH_BINARY+ cv2.THRESH_OTSU)

# Kontur bulma
contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Konturları çizme, alan hesabı yapma ve centroid bulma
img_contours = img.copy()

# Her bir kontur için işlemleri yapma
for contour in contours:
    cv2.drawContours(img_contours, [contour], -1, (0, 255, 0), 2)
    
    # Alan hesabı yapma
    area = cv2.contourArea(contour)
    print("Alan:", area)
    
    # Sınırlayıcı dikdörtgeni oluşturma
    x, y, w, h = cv2.boundingRect(contour)
    # Dikdörtgenin koordinat bilgilerini sol üst köşeye yazdırma
   
    # Dikdörtgeni çizme
    cv2.rectangle(img_contours, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    # Ağırlık merkezini (centroid) bulma
    M = cv2.moments(contour)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    
    # Ağırlık merkezine kırmızı bir nokta eklemek
    cv2.circle(img_contours, (cX, cY), 5, (0, 0, 255), -1)
    
    # En küçük çevreleyen çemberin merkezini ve yarıçapını bulma
    (l, k), radius = cv2.minEnclosingCircle(contour)
    center = (int(l), int(k))
    radius = int(radius)
    
    # En küçük çevreleyen çembreyi çizme
    cv2.circle(img_contours, center, radius, (0, 255, 0), 2)
    cv2.circle(img_contours, center, 5, (0, 255, 255), 3)
    cv2.line(img_contours, center, (center[0], center[1]+radius), (0, 0, 255), 2)
    cv2.line(img_contours, center, (center[0], center[1]-radius), (0, 0, 255), 2)
    cv2.line(img_contours, center, (center[0]+radius, center[1]), (0, 0, 255), 2)
    cv2.line(img_contours, center, (center[0]-radius, center[1]), (0, 0, 255), 2)

# Görüntüleri gösterme
cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresh)
cv2.imshow('Contours', img_contours)

cv2.waitKey(0)
cv2.destroyAllWindows()
