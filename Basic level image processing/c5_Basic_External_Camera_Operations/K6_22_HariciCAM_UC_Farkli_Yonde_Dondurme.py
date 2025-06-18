# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 00:41:48 2024

@author: muozi
"""
import cv2

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture(2)

# Flip kombinasyonlarını uygula ve ekranda göster
while True:
    # Kameradan görüntüyü al
    ret, goruntu = kamera.read()

    # Orjinal görüntüyü kırmızı renkte yazdır
    goruntu2=goruntu.copy()
    goruntu3 = cv2.putText(goruntu2, 'Original', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow('Original', goruntu3)

    # 0: X ekseninde dönme (yatay simetri).
    flipped_image_0 = cv2.flip(goruntu, 0)
    flipped_image_0_red = cv2.putText(flipped_image_0, 'Flipped WebCam 0 X ekseninde donme(yatay simetri)', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow('Flipped WebCam 0 X ekseninde donme(yatay simetri)', flipped_image_0_red)

    # 1: Y ekseninde dönme (dikey simetri).
    flipped_image_1 = cv2.flip(goruntu, 1)
    flipped_image_1_red = cv2.putText(flipped_image_1, 'Flipped WebCam 1 Y ekseninde donme (dikey simetri)', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow('Flipped WebCam 1 Y ekseninde donme (dikey simetri)', flipped_image_1_red)

    # X ve Y eksenlerinde dönüş
    flipped_image_2 = cv2.flip(goruntu, -1)
    flipped_image_2_red = cv2.putText(flipped_image_2, 'Flipped WebCam 2 X ve Y eksenlerinde donus', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow('Flipped WebCam 2 X ve Y eksenlerinde donus', flipped_image_2_red)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
kamera.release()
# Tüm pencereleri kapat
cv2.destroyAllWindows()


