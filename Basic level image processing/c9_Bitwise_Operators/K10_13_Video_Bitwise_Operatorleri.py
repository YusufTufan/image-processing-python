# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:33:40 2024

@author: muozi
"""

import cv2

# Video dosyasını oku
cap = cv2.VideoCapture('Video_Trafic.mp4')

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
    _, thresh_frame_inv = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY_INV)
    _, thresh_frame_tozero = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_TOZERO)
    _, thresh_frame_tozero_inv = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_TOZERO_INV)
    _, thresh_frame_trunc = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_TRUNC)

    bit_and = cv2.bitwise_and(gray_frame, thresh_frame_inv)
    not_img1 = cv2.bitwise_not(frame)
    cv2.imshow("not_img1", not_img1)


    cv2.imshow("bit_and", bit_and)
    cv2.imshow("gray_frame", gray_frame)


    
    
    
    # Eşiklenmiş çerçeveleri göster
    # cv2.imshow("Video_Trafic", frame)
    # cv2.imshow("Basit Thresholding (127)", thresh_frame_127)
    cv2.imshow("Thresholding Inverted", thresh_frame_inv)
    # cv2.imshow("Thresholding To Zero", thresh_frame_tozero)
    # cv2.imshow(" Thresholding To Zero Inverted", thresh_frame_tozero_inv)
    # cv2.imshow(" Thresholding Truncated", thresh_frame_trunc)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Videoyı serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()