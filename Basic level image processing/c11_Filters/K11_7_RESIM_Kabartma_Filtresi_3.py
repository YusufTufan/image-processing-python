# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:21:46 2024

@author: muozi
"""

import cv2
import numpy as np

# Görüntüyü yükle
img = cv2.imread('Resim18_Bitewing2.jpg')

# Gri tonlamalı hale getir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Görüntü boyutları
height, width = gray.shape

# Ortak bir 128 gri değeri olan bir matris oluştur
y = np.ones((height, width), np.uint8) * 128

# Dört farklı yöne doğru emboss etkisi sağlayan kernel'ları oluştur
kernel_south_to_north = np.array([[1, 1, 1],
                                  [0, 0, 0],
                                  [-1, -1, -1]])

kernel_southeast_to_northwest = np.array([[0, 1, 1],
                                           [-1, 0, 1],
                                           [-1, -1, 0]])

kernel_east_to_west = np.array([[-1, 0, 1],
                                 [-1, 0, 1],
                                 [-1, 0, 1]])

kernel_southwest_to_northeast = np.array([[-1, -1, 0],
                                           [-1, 0, 1],
                                           [0, 1, 1]])

# 45 derece dönüş açısına sahip emboss filtreler oluştur
kernel_southwest_to_northeast_45 = np.array([[-1, -1, 2],
                                             [-1, 2, -1],
                                             [2, -1, -1]])

kernel_northeast_to_southwest_45 = np.array([[2, -1, -1],
                                             [-1, 2, -1],
                                             [-1, -1, 2]])

# Her bir yöne emboss etkisi uygula
output_south_to_north = cv2.filter2D(gray, -1, kernel_south_to_north)
output_southeast_to_northwest = cv2.filter2D(gray, -1, kernel_southeast_to_northwest)
output_east_to_west = cv2.filter2D(gray, -1, kernel_east_to_west)
output_southwest_to_northeast = cv2.filter2D(gray, -1, kernel_southwest_to_northeast)
output_southwest_to_northeast_45 = cv2.filter2D(gray, -1, kernel_southwest_to_northeast_45)
output_northeast_to_southwest_45 = cv2.filter2D(gray, -1, kernel_northeast_to_southwest_45)

# Her bir emboss sonucunu 128 gri değeri ile ekleyerek birleştir
output = cv2.add(output_south_to_north, y)
output = cv2.add(output, output_southeast_to_northwest)
output = cv2.add(output, output_east_to_west)
output = cv2.add(output, output_southwest_to_northeast)
output = cv2.add(output, output_southwest_to_northeast_45)
output = cv2.add(output, output_northeast_to_southwest_45)

# Görüntüleri göster
cv2.imshow("Image", img)
cv2.imshow("South to North", output_south_to_north)
cv2.imshow("Southeast to Northwest", output_southeast_to_northwest)
cv2.imshow("East to West", output_east_to_west)
cv2.imshow("Southwest to Northeast", output_southwest_to_northeast)
cv2.imshow("Southwest to Northeast 45", output_southwest_to_northeast_45)
cv2.imshow("Northeast to Southwest 45", output_northeast_to_southwest_45)
cv2.imshow("Combined Output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
