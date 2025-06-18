import cv2
import numpy as np

kamera= cv2.VideoCapture('Video_Trafic.mp4')

while(1):
    ret, frame=kamera.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


       
    dusuk_gri = np.array([0, 0, 100])    # Alt sınır (düşük doygunluk, orta parlaklık)
    ust_gri = np.array([180, 60, 200])   # Üst sınır (geniş hue aralığı, düşük doygunluk, orta-yüksek parlaklık)
    mask=cv2.inRange(hsv,dusuk_gri,ust_gri)
    son_resim=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('orjinal',frame)
    cv2.imshow('mask', mask)
    cv2.imshow('son_resim', son_resim)


    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()