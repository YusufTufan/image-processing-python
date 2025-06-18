# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 04:47:51 2024

@author: muozi
"""

import numpy as np
import cv2
import requests

url = "http://192.168.92.65:8080//shot.jpg"

while True:
    # Kameradan görüntüyü al
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    frame = cv2.resize(img, (960, 540))
    
    # Çerçeveyi gri tonlamaya çevir
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Basit thresholding (127)
    _, thresh_frame_127 = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)

    # Adaptive thresholding (MEAN_C)
    thresh_frame_mean = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

    # Adaptive thresholding (GAUSSIAN_C)
    thresh_frame_gaussian = cv2.adaptiveThreshold(gray_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Otsu thresholding
    _, thresh_frame_otsu = cv2.threshold(gray_frame, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Eşiklenmiş çerçeveleri göster
    cv2.imshow("Video_Trafic", frame)
    cv2.imshow("Basit Thresholding (127)", thresh_frame_127)
    cv2.imshow("Adaptive Thresholding (MEAN_C)", thresh_frame_mean)
    cv2.imshow("Adaptive Thresholding (GAUSSIAN_C)", thresh_frame_gaussian)
    cv2.imshow("Otsu Thresholding", thresh_frame_otsu)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
