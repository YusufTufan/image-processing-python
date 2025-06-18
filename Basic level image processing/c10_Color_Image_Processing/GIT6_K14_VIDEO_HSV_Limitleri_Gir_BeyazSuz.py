import cv2
import numpy as np

kamera= cv2.VideoCapture('Video_Trafic.mp4')

while(1):
    ret, frame=kamera.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


       
    dusuk_beyaz = np.array([0, 0, 200])    # Alt sınır (beyaz için düşük doygunluk ve yüksek parlaklık)
    ust_beyaz = np.array([180, 40, 255])   # Üst sınır (beyaz için herhangi bir hue değeri, düşük doygunluk ve yüksek parlaklık)
    mask=cv2.inRange(hsv,dusuk_beyaz,ust_beyaz)
    son_resim=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('orjinal',frame)
    cv2.imshow('mask', mask)
    cv2.imshow('son_resim', son_resim)


    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()