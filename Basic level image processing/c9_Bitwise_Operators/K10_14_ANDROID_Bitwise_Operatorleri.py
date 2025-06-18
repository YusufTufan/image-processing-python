# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:26:47 2024

@author: muozi
"""

import numpy as np
import os
import cv2
import requests

url = "http://192.168.1.3:8080//shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    image = cv2.resize(img, (960, 540))
    
    gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh_frame_127 = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)
    _, thresh_frame_inv = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY_INV)
    _, thresh_frame_tozero = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_TOZERO)
    _, thresh_frame_tozero_inv = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_TOZERO_INV)
    _, thresh_frame_trunc = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_TRUNC)

    bit_and = cv2.bitwise_and(gray_frame, thresh_frame_inv)
    cv2.imshow("bit_and", bit_and)
    cv2.imshow("gray_frame", gray_frame)

    cv2.imshow("Video_Traffic", image)
    cv2.imshow("Basit Thresholding (127)", thresh_frame_127)
    cv2.imshow("Otsu Thresholding Inverted", thresh_frame_inv)
    cv2.imshow("Otsu Thresholding To Zero", thresh_frame_tozero)
    cv2.imshow("Otsu Thresholding To Zero Inverted", thresh_frame_tozero_inv)
    cv2.imshow("Otsu Thresholding Truncated", thresh_frame_trunc)

    if cv2.waitKey(1) & 0xFF == ord("q"): 
        break

cv2.destroyAllWindows()
