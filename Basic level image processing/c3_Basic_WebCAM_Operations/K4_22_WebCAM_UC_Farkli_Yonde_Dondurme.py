# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 00:41:48 2024

@author: muozi
"""

import cv2

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture(0)

# Flip kombinasyonlarını uygula ve ekranda göster
while True:
    # Kameradan görüntüyü al
    ret, goruntu = kamera.read()

    # 0: X ekseninde dönme (yatay simetri).
    flipped_image_0 = cv2.flip(goruntu, 0)
    cv2.imshow('Flipped WebCam 0 X ekseninde donme(yatay simetri)', flipped_image_0)

    # 1: Y ekseninde dönme (dikey simetri).
    flipped_image_1 = cv2.flip(goruntu, 1)
    cv2.imshow('Flipped WebCam 1 Y ekseninde donme (dikey simetri)', flipped_image_1)

    # X ve Y eksenlerinde dönüş
    flipped_image_2 = cv2.flip(goruntu, -1)
    cv2.imshow('Flipped WebCam 2 X ve Y eksenlerinde donus', flipped_image_2)

    # -1: Hem X hem de Y eksenlerinde dönme (hem yatay hem de dikey simetri).
  
    cv2.imshow('Original', goruntu)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
kamera.release()
# Tüm pencereleri kapat
cv2.destroyAllWindows()

