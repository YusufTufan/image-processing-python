# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:41:49 2024

@author: muozi
"""

import cv2

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture(0)

while True:
    # Kameradan görüntüyü al
    ret, goruntu = kamera.read()
    
    # Görüntü boyutunu al
    yukseklik, genislik = goruntu.shape[:2]
    
    # Metni görüntünün üstüne yazdır
    metin = f'Genislik(sutun): {genislik}px, Yukseklik(satir): {yukseklik}px'
    cv2.putText(goruntu, metin, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Görüntüyü göster
    cv2.imshow('WebCam', goruntu)
    
    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
kamera.release()
# Tüm pencereleri kapat
cv2.destroyAllWindows()
