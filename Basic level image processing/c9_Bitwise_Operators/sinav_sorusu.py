# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 02:35:31 2024

@author: muozi
"""

import cv2

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()

    if not ret:
        
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    gray_frame = cv2.medianBlur(gray_frame, 5)

    
    gray_frame = cv2.blur(gray_frame, (11, 11)) 

    
    _, thresh_frame_tozero_inv = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_TOZERO_INV)
   

    bit_and = cv2.bitwise_and(gray_frame, thresh_frame_tozero_inv)
    
        
    bit_and = cv2.Canny(bit_and, 100, 200)
    
    
    cv2.imshow("bit_and", bit_and)
    
    cv2.imshow("gray_frame", gray_frame)


    if cv2.waitKey(25) & 0xFF == ord("q"):
        
        break

cap.release()

cv2.destroyAllWindows()