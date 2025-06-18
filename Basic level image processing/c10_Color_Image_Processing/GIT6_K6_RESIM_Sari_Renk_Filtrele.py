import cv2
import numpy as np

img=cv2.imread('R1_Sari_Kirmizi.jpg')
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

dusuk_sari=np.array([16,36,0])
ust_sari=np.array([32,255,255])
mask=cv2.inRange(hsv,dusuk_sari,ust_sari)



son_resim=cv2.bitwise_and(img,img,mask=mask)

cv2.imshow('img',img)
cv2.imshow('mask', mask)
cv2.imshow('son_resim', son_resim)


cv2.imshow('hsv',hsv)
  
cv2.waitKey(0)
cv2.destroyAllWindows()