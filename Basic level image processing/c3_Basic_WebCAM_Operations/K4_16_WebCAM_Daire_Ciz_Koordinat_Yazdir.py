# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:07:02 2024

@author: muozi
"""

import cv2

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture(0)

while True:
    # Kameradan görüntüyü al
    ret, goruntu = kamera.read()

    # Görüntüye çizgi ekle
    cv2.circle(goruntu,(200,200),100,(0,0,255),3)

    # Çizginin başlangıç ve bitiş koordinatlarını oluştur
    Merkez = (200, 200)
    Radius = (320, 160)

    # Çizginin başlangıç ve bitiş koordinatlarını görüntünün altına yazdır
    cv2.putText(goruntu, f'Baslangic: {Merkez}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    cv2.putText(goruntu, f'Bitis: {Radius}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    # Görüntüyü göster
    cv2.imshow('WebCam', goruntu)
    
    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
kamera.release()
# Tüm pencereleri kapat
cv2.destroyAllWindows()