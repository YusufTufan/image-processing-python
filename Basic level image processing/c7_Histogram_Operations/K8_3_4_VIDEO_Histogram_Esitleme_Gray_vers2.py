# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 06:00:51 2024

@author: muozi
"""

import cv2

# Video dosyasını oku
cap = cv2.VideoCapture("Video_Trafic.mp4")

while True:
    # Bir sonraki çerçeveyi oku
    ret, frame = cap.read()

    # Eğer çerçeve alınamazsa döngüden çık
    if not ret:
        break

    # Renkli çerçeveyi gri tonlamaya çevir
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gri tonlamalı çerçeveyi histogram eşitle
    eq_gray_frame = cv2.equalizeHist(gray_frame)

    # Orijinal ve eşitlenmiş gri tonlamalı görüntüleri göster
    cv2.imshow("Orjinal Gri Görüntü", gray_frame)
    cv2.imshow("Histogram Eşitleme Sonrası Gri Görüntü", eq_gray_frame)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Videoyı serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
