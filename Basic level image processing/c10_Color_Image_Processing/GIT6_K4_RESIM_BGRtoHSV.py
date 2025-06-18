# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 14:22:56 2023

@author: MUOZIC
"""


import cv2

img = cv2.imread('R1_Sari_Kirmizi.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(img_hsv)

cv2.imshow("RENKLI", img)
cv2.imshow("Hue Kanali", h)
cv2.imshow("Saturation Kanali", s)
cv2.imshow("Value Kanali", v)

cv2.waitKey(0)
cv2.destroyAllWindows()
