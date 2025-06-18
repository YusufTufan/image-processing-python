# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:05:19 2024

@author: muozi
"""

import cv2

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture(0)

while True:
    # Kameradan görüntüyü al
    ret, goruntu = kamera.read()

    # Görüntü veri tipini al
    veri_tipi = goruntu.dtype

 

    # Veri tipini görüntünün üstüne yazdır
    cv2.putText(goruntu, f'Veri Tipi: {veri_tipi}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    # Görüntüyü göster
    cv2.imshow('WebCam', goruntu)
    
    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
kamera.release()
# Tüm pencereleri kapat
cv2.destroyAllWindows()
