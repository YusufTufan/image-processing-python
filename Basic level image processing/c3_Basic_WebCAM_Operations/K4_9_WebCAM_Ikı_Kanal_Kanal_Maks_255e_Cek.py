# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:16:21 2024

@author: muozi
"""


import cv2

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture(0)

while True:
    # Kameradan görüntüyü al
    ret, goruntu = kamera.read()

    cv2.imshow('WebCam', goruntu)

    goruntu[:,:,0]=255
    goruntu[:,:,1]=255

    # Görüntüyü göster
    cv2.imshow('WebCam_Mavi_Max', goruntu)
    
    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
kamera.release()
# Tüm pencereleri kapat
cv2.destroyAllWindows()