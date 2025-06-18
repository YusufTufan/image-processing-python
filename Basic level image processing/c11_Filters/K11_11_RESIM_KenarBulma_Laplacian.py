# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 02:09:05 2023

@author: MUOZIC
"""



import cv2
from matplotlib import pyplot as plt

# Resmi siyah beyaz olarak yükle
img = cv2.imread('Resim1_Dort_Nohut.png', 0)

# Laplacian kenar tespiti uygula
# laplacian = cv2.Laplacian(img, cv2.CV_64F,ksize=3)
laplacian = cv2.Laplacian(img, cv2.CV_8U,ksize=5)


# Görüntüleri göster
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(1, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.show()




