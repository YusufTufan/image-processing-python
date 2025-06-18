# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 04:26:13 2024

@author: muozi
"""

import cv2
import numpy as np

# Video dosyasını oku
cap = cv2.VideoCapture(0)

while True:
    # Bir sonraki çerçeveyi oku
    ret, frame = cap.read()

    # Eğer çerçeve alınamazsa döngüden çık
    if not ret:
        break

    # Çerçeveyi gri tonlamaya çevir
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Basit thresholding (127)
    _, thresh_frame_127 = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)

    # Adaptive thresholding (MEAN_C)
    thresh_frame_mean = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 115, 2)

    # Adaptive thresholding (GAUSSIAN_C)
    thresh_frame_gaussian = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 2)

    # Otsu thresholding
    _, thresh_frame_otsu = cv2.threshold(gray_frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Eşiklenmiş çerçeveleri göster
    cv2.imshow("Video_Trafic", frame)
    cv2.imshow("Basit Thresholding (127)", thresh_frame_127)
    cv2.imshow("Adaptive Thresholding (MEAN_C)", thresh_frame_mean)
    cv2.imshow("Adaptive Thresholding (GAUSSIAN_C)", thresh_frame_gaussian)
    cv2.imshow("Otsu Thresholding", thresh_frame_otsu)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Videoyı serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()
