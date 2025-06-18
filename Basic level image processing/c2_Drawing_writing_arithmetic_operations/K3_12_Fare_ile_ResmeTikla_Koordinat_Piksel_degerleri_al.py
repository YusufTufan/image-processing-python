# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:33:10 2023

@author: muozi
"""

import cv2
import numpy as np

# Fare tıklama işlemi için bir işlev tanımlayın
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Tıklanan pikselin değerini alın
        b, g, r = img[y, x]
        print(f"Koordinat: ({x}, {y}) - Piksel Değerleri: B={b}, G={g}, R={r}")

# Boş bir görüntü oluşturun veya mevcut bir görüntüyü yükleyin
# img = np.zeros((512, 512, 3), np.uint8)  # 512x512 boyutunda siyah bir görüntü
img = cv2.imread('bee.jpg')  # Mevcut bir resim yüklemek için bu satırı kullanabilirsiniz

# Görüntüyü görüntüleyin
cv2.imshow('Görüntü', img)

# Fare olaylarını dinlemek için bir işlev bağlayın
cv2.setMouseCallback('Görüntü', click_event)

while True:
    if cv2.waitKey(1) & 0xFF == 27:  # ESC tuşuna basarak pencereyi kapatın
        break

cv2.destroyAllWindows()