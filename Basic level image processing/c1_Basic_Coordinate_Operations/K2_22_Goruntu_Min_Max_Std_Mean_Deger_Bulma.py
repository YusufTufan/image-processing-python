# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 00:20:28 2024

@author: muozi
"""

import cv2
import numpy as np

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)


img1=cv2.imread('bee.jpg',0)
cv2.imshow('bee1',img1)


# Minimum piksel değeri
min_val = np.min(img)

# Maksimum piksel değeri
max_val = np.max(img)

# Ortalama piksel değeri
mean_val = np.mean(img)

# Standart sapma
std_dev = np.std(img)

# Sonuçları yazdır
print("Minimum Piksel Değeri:", min_val)
print("Maksimum Piksel Değeri:", max_val)
print("Ortalama Piksel Değeri:", mean_val)
print("Standart Sapma:", std_dev)


# Minimum piksel değeri
min_val1 = np.min(img1)

# Maksimum piksel değeri
max_val1 = np.max(img1)

# Ortalama piksel değeri
mean_val1 = np.mean(img1)

# Standart sapma
std_dev1 = np.std(img1)

# Sonuçları yazdır
print("Minimum Piksel Değeri1:", min_val1)
print("Maksimum Piksel Değeri1:", max_val1)
print("Ortalama Piksel Değeri1:", mean_val1)
print("Standart Sapma1:", std_dev1)

rounded_mean_val = round(mean_val1, 2)
print("Ortalama Piksel Değeri (Yuvarlanmış):", rounded_mean_val)



cv2.waitKey(0)
cv2.destroyAllWindows()