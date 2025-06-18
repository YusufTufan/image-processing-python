# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:01:50 2024

@author: muozi
"""

import cv2

img=cv2.imread('bee.jpg')
cv2.imshow('bee',img)


img1=cv2.imread('bee.jpg',0)
cv2.imshow('bee1',img1)


print("175. satir ve 175.sütun mavi kanal pixel degeri:"+str(img.item(175,175,0))) #BLUE
print("175. satir ve 175.sütun yesil kanal pixel degeri:"+str(img.item(175,175,1))) #GREEN
print("175. satir ve 175.sütun kirmizi kanal pixel degeri:"+str(img.item(175,175,2))) #RED

print("175. satir ve 175.sütun gri seviye pixel degeri:"+str(img1.item(150,150))) #GRAY


cv2.waitKey(0)
cv2.destroyAllWindows()