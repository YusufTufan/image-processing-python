# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:24:10 2024

@author: muozi
"""


import cv2

# 'bee.jpg' adlı bir görüntü dosyası OpenCV ile yüklenir
img = cv2.imread('bee.jpg')

# Renkli olarak yüklenen görüntü ekranda gösterilir
cv2.imshow('bee', img)

# 'bee.jpg' adlı bir görüntü dosyası gri tonlamalı olarak yüklenir
img1 = cv2.imread('bee.jpg', 0)

# Gri tonlamalı olarak yüklenen görüntü ekranda gösterilir
cv2.imshow('bee1', img1)

# Renkli görüntüden belirli bir ROI (Region of Interest) seçilir ve ekranda gösterilir
# img1[200:270, 150:220] ifadesi, NumPy dizinleme yöntemini kullanır.
# Bu ifade, iki boyutlu bir dizide belirli bir bölgeyi seçmek için kullanılır. 
# img1 adlı dizide, 200 ile 269 (dahil) arasındaki satırları ve 150 ile 219 (dahil) arasındaki sütunları seçer.


ROI = img[200:270, 150:220]  # Belirli bir bölgeyi (ROI) seç
cv2.imshow('roi', ROI)

# Gri tonlamalı görüntüden belirli bir ROI (Region of Interest) seçilir ve ekranda gösterilir
ROI2 = img1[200:270, 150:220]  # Belirli bir bölgeyi (ROI) seç
cv2.imshow('roi2', ROI2)

# Renkli görüntüde seçilen ROI'yi başka bir yere yerleştirir
img[270:340, 150:220] = ROI
cv2.imshow('img', img)

# Gri tonlamalı görüntüde seçilen ROI'yi başka bir yere yerleştirir
img1[270:340, 150:220] = ROI2
cv2.imshow('img1', img1)

# Bir tuşa basılana kadar beklenir ve tüm pencereler kapatılır
cv2.waitKey(0)
cv2.destroyAllWindows()
