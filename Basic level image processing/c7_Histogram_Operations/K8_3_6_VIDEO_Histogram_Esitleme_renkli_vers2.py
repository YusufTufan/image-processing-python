# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 05:58:41 2024

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

    # Renkli görüntüyü böl ve her bir kanalı eşitle
    b, g, r = cv2.split(frame)
    b_eq = cv2.equalizeHist(b)
    g_eq = cv2.equalizeHist(g)
    r_eq = cv2.equalizeHist(r)

    # Eşitlenmiş kanalları birleştir
    frame_eq = cv2.merge((b_eq, g_eq, r_eq))

    # Orijinal ve eşitlenmiş görüntüleri göster
    cv2.imshow("Orjinal Görüntü", frame)
    cv2.imshow("Histogram Eşitleme Sonrası Görüntü", frame_eq)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

# Videoyı serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()

