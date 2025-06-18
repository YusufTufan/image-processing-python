# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 08:00:49 2024

@author: muozi
"""

import cv2

def renk_sec(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_degerleri = hsv_goruntu[y, x]
        print("HSV Değerleri:", hsv_degerleri)

goruntu = cv2.imread('Kitap.jpg')
hsv_goruntu = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)

cv2.imshow('Ornek Goruntu', goruntu)
cv2.setMouseCallback('Ornek Goruntu', renk_sec)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

