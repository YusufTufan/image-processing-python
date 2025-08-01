# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:53:40 2024

@author: muozi
"""

import cv2

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture('Video_Trafic.mp4')

while True:
    # Kameradan görüntüyü al
    ret, goruntu = kamera.read()

    # Görüntüyü göster
    
    cv2.rectangle(goruntu,(200,70),(400,300),(0,0,255),2)
    cv2.imshow('WebCam', goruntu)
    
    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
kamera.release()
# Tüm pencereleri kapat
cv2.destroyAllWindows()