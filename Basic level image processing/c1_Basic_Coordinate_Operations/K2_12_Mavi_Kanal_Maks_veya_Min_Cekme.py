# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:34:22 2024

@author: muozi
"""


import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)



img[:,:,0]=0


cv2.imshow('blue_sifira_cek',img)



img[:,:,0]=225


cv2.imshow('blue_maks__doyuma_cek',img)






cv2.waitKey(0)
cv2.destroyAllWindows()