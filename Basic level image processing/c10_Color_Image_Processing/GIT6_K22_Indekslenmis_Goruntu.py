# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 09:31:51 2024

@author: muozi
"""

import numpy as np
import cv2

# 1. Renk Paletini Tanımla (4 renk)
color_palette = np.array([
    [0, 0, 255],  # Kırmızı (Red)
    [0, 255, 0],  # Yeşil (Green)
    [255, 0, 0],  # Mavi (Blue)
    [0, 255, 255] # Sarı (Yellow)
], dtype=np.uint8)

# 2. İndeklenmiş Görüntü Oluştur
indexed_image = np.array([
    [0, 1, 2, 3, 0],
    [1, 2, 3, 0, 1],
    [2, 3, 0, 1, 2],
    [3, 0, 1, 2, 3],
    [0, 1, 2, 3, 0]
], dtype=np.uint8)

# 3. Renk Paletinden İlgili Renkleri Seç
rgb_image = color_palette[indexed_image]

# 4. Görüntü Boyutlarını Büyüt
# Resmin her pikselini daha büyük hale getirmek için cv2.resize kullanıyoruz.
# Örneğin, görüntüyü 100x100 piksel boyutlarına çıkaracağız.
large_image = cv2.resize(rgb_image, (500, 500), interpolation=cv2.INTER_NEAREST)

# 5. Görüntüyü Görselleştir
cv2.imshow('Larger Indexed Image', large_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6. Görüntüyü Kaydet
