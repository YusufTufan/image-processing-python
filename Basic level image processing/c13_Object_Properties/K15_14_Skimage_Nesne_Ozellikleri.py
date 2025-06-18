# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:46:11 2024

@author: muozi
"""

import numpy as np
import cv2
from skimage import measure

# Görüntüyü yükleyin
img = cv2.imread('img1_Dort_Nohut.png')

# Görüntüyü gri tonlamaya çevirin ve bulanıklaştırın
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.blur(gray, (5, 5))

# İkili eşikleme işlemi yapın
_, thresh = cv2.threshold(gray_blurred, 50, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# İkili görüntüyü etiketleyin
labels = measure.label(thresh, connectivity=2, background=0)

# Görüntülenebilir hale getirin: labels'i 8-bit formatına dönüştürün
labels_display = (labels * (255 / labels.max())).astype(np.uint8)

# Her bir nesnenin özelliklerini bulun ve tüm özellikleri yazdırın
properties = measure.regionprops(labels, intensity_image=gray)

for i, prop in enumerate(properties, start=1):
    print(f"Nesne {i} Özellikleri:")
    print(f"Etiket: {prop.label}")
    print(f"Alan: {prop.area}")
    print(f"Bounding Box: {prop.bbox}")
    print(f"Bounding Box Alanı: {prop.bbox_area}")
    print(f"Merkez (Centroid): {prop.centroid}")
    print(f"Konveks Alan: {prop.convex_area}")
    print(f"Çevre: {prop.perimeter}")
    print(f"Merkez (Centroid): {prop.centroid}")
    print(f"Eksantriklik (Eccentricity): {prop.eccentricity}")
    print(f"Eşdeğer Çap: {prop.equivalent_diameter}")
    print(f"Euler Sayısı: {prop.euler_number}")
    print(f"Extent (Dolu Alan Oranı): {prop.extent}")
    print(f"Doldurulmuş Alan: {prop.filled_area}")
    print(f"Büyük Eksen Uzunluğu: {prop.major_axis_length}")
    print(f"Küçük Eksen Uzunluğu: {prop.minor_axis_length}")
    print(f"Maksimum Yoğunluk: {prop.max_intensity if hasattr(prop, 'max_intensity') else 'N/A'}")
    print(f"Ortalama Yoğunluk: {prop.mean_intensity if hasattr(prop, 'mean_intensity') else 'N/A'}")
    print(f"Minimum Yoğunluk: {prop.min_intensity if hasattr(prop, 'min_intensity') else 'N/A'}")
    print(f"Açısal Yönelim: {prop.orientation}")
    print(f"İnertia Tensor: {prop.inertia_tensor}")
    print(f"Inertia Tensor Özdeğerleri: {prop.inertia_tensor_eigvals}")
    print(f"Solidity: {prop.solidity}")
    print(f"Ağırlıklı Merkez (Weighted Centroid): {prop.weighted_centroid}")
    print(f"Weighted Local Centroid: {prop.weighted_local_centroid}")
    print(f"Weighted Moments: {prop.weighted_moments}")
    print(f"Weighted Central Moments: {prop.weighted_moments_central}")
    print(f"Weighted Hu Moments: {prop.weighted_moments_hu}")
    print(f"Weighted Normalized Moments: {prop.weighted_moments_normalized}")
    print("-" * 40)

# Görüntüleri gösterin
cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresh)
cv2.imshow('Labels', labels_display)

cv2.waitKey(0)
cv2.destroyAllWindows()

