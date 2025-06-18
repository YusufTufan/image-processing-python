import cv2
import numpy as np

kamera= cv2.VideoCapture('Video_Trafic.mp4')

while(1):
    ret, frame=kamera.read()

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # dusuk_mavi=np.array([100,60,60])
    # ust_mavi=np.array([140,255,255])
    # mask=cv2.inRange(hsv,dusuk_mavi,ust_mavi)
    # son_resim=cv2.bitwise_and(frame,frame,mask=mask)
       
    dusuk_kirmizi=np.array([150,30,30])
    ust_kirmizi=np.array([190,255,255])
    mask=cv2.inRange(hsv,dusuk_kirmizi,ust_kirmizi)
    son_resim=cv2.bitwise_and(frame,frame,mask=mask)
    
    # dusuk_kirmizi=np.array([0,0,112])
    # ust_kirmizi=np.array([89,255,255])
    # mask=cv2.inRange(hsv,dusuk_kirmizi,ust_kirmizi)
    # son_resim=cv2.bitwise_and(frame,frame,mask=mask)
    
    # dusuk_beyaz=np.array([150,30,30])
    # ust_beyaz=np.array([190,255,255])   
    # mask=cv2.inRange(hsv,dusuk_beyaz,ust_beyaz)
    # son_resim=cv2.bitwise_and(frame,frame,mask=mask)
    
    # dusuk_sari=np.array([150,30,30])
    # ust_sari=np.array([190,255,255])
    # mask=cv2.inRange(hsv,dusuk_sari,ust_sari)
    # son_resim=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('orjinal',frame)
    cv2.imshow('mask', mask)
    cv2.imshow('son_resim', son_resim)


    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()