# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:40:28 2024

@author: muozi
"""

import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)


img[:,:,1]=0
img[:,:,2]=0


cv2.imshow('kirmizi_yesil_sifira_cek',img)



img[:,:,1]=225
img[:,:,2]=225


cv2.imshow('kirmizi_yesil_maks__doyuma_cek',img)






cv2.waitKey(0)
cv2.destroyAllWindows()