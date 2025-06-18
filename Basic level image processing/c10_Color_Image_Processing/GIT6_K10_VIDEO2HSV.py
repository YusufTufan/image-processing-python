import cv2


cap = cv2.VideoCapture("Video_Trafic.mp4")



while True:
    ret, frame = cap.read()

    if ret == 0:
        break
    
    
    frame2=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    cv2.imshow("IndiaTrafic", frame)
    cv2.imshow("IndiaTrafic_HSV", frame2)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()