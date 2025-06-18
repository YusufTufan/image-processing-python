# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 04:45:59 2024

@author: muozi
"""

import numpy as np
import os
import cv2
import requests

url = "http://192.168.92.65:8080//shot.jpg"

while True:
    # Kameradan görüntüyü al
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    image = cv2.resize(img, (960, 540))
    
    # Gri tonlamaya çevir
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Basit thresholding (127)
    _, thresh_frame_127 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Otsu thresholding
    _, thresh_frame_otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    _, thresh_frame_otsu_inv = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    _, thresh_frame_tozero = cv2.threshold(gray, 0, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
    _, thresh_frame_tozero_inv = cv2.threshold(gray, 0, 255, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)
    _, thresh_frame_trunc = cv2.threshold(gray, 0, 255, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)

    # Eşiklenmiş çerçeveleri göster
    cv2.imshow("Video_Trafic", image)
    cv2.imshow("Basit Thresholding (127)", thresh_frame_127)
    cv2.imshow("Otsu Thresholding", thresh_frame_otsu)
    cv2.imshow("Otsu Thresholding Inverted", thresh_frame_otsu_inv)
    cv2.imshow("Otsu Thresholding To Zero", thresh_frame_tozero)
    cv2.imshow("Otsu Thresholding To Zero Inverted", thresh_frame_tozero_inv)
    cv2.imshow("Otsu Thresholding Truncated", thresh_frame_trunc)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
