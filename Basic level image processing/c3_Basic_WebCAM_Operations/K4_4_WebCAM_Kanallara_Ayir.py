# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:57:59 2024

@author: muozi
"""

import cv2

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture(0)

while True:
    # Kameradan görüntüyü al
    ret, goruntu = kamera.read()
    
    # Görüntüyü BGR kanallarına ayır
    blue, green, red = cv2.split(goruntu)
    
    
    cv2.imshow('Original', goruntu)

    # Kanalları ayrı ayrı pencerelerde göster
    cv2.imshow('Blue Channel', blue)
    cv2.imshow('Green Channel', green)
    cv2.imshow('Red Channel', red)
    
    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
kamera.release()
# Tüm pencereleri kapat
cv2.destroyAllWindows()
