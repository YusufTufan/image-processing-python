# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 04:44:03 2024

@author: muozi
"""

import numpy as np
import os
import cv2
import requests

url = "http://10.156.63.132:8080//shot.jpg"

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
    _, thresh_frame_inv = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    _, thresh_frame_tozero = cv2.threshold(gray, 50, 255, cv2.THRESH_TOZERO)
    _, thresh_frame_tozero_inv = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)
    _, thresh_frame_trunc = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)

    # Eşiklenmiş çerçeveleri göster
    cv2.imshow("Android", image)
    cv2.imshow("Basit Thresholding (127)", thresh_frame_127)
    cv2.imshow("Thresholding Inverted", thresh_frame_inv)
    cv2.imshow("Thresholding To Zero", thresh_frame_tozero)
    cv2.imshow("Thresholding To Zero Inverted", thresh_frame_tozero_inv)
    cv2.imshow("Thresholding Truncated", thresh_frame_trunc)

    # 'q' tuşuna basıldığında döngüyü sonlandır
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
