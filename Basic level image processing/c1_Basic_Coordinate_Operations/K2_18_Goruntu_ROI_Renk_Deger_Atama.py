# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 00:30:36 2024

@author: muozi
"""

import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)


# img1=cv2.imread('bee.jpg',0)
# cv2.imshow('bee1',img1)



# img[270:340,150:220]=255
# cv2.imshow('img',img)

# img1[270:340,150:220]=255
# cv2.imshow('img1',img1)

# img[270:340,150:220]=200
# cv2.imshow('img',img)

# img1[270:340,150:220]=200
# cv2.imshow('img1',img1)

#5Belirtilen aralığı tamamen kırmızı yap
img[200:300,150:220]=(130, 201, 85)
cv2.imshow('img',img)

#5Belirtilen aralığı tamamen yeşil yap

img[340:400,300:350]=(0, 0, 0)
cv2.imshow('img',img)

cv2.imwrite('banlı.png', img)

cv2.waitKey(0)
cv2.destroyAllWindows()