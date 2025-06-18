# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:21:35 2024

@author: muozi
"""

import cv2

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture(0)

while True:
    # Kameradan görüntüyü al
    ret, goruntu = kamera.read()
    
    # Görüntüyü gri tonlamalı olarak dönüştür
    griton = cv2.cvtColor(goruntu, cv2.COLOR_BGR2GRAY)

    # Renkli ve gri tonlamalı görüntüyü göster
    cv2.imshow('WebCAM_Renkli', goruntu)
    cv2.imshow('WebCAM_GriTon', griton)
    
    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
kamera.release()
# Tüm pencereleri kapat
cv2.destroyAllWindows()
