import numpy as np
import os
import cv2
import requests
url = "http://192.168.1.12:8080//shot.jpg"

        
while True:
    
    
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    # image = cv2.resize(img, (640, 480))
    image = cv2.resize(img, (1920, 1080))

    
    
    cv2.putText(image, 'Android', (10,30),cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255),2)
            
    
    
    

    
    cv2.imshow("ssd",image)
    
    
    
    if cv2.waitKey(1) & 0xFF == ord("q"): 
        break
    
    
cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    