# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:38:58 2024

@author: muozi
"""

import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)



img[:,:,2]=0


cv2.imshow('kirmizi_sifira_cek',img)



img[:,:,2]=225


cv2.imshow('kirmizi_maks__doyuma_cek',img)






cv2.waitKey(0)
cv2.destroyAllWindows()