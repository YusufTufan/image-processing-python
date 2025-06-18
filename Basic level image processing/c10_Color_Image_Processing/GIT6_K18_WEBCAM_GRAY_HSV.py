import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret == 0:
        break
    
    frame2=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    cv2.imshow("WebCAM", frame)
    cv2.imshow("hsv", hsv)
    cv2.imshow("WebCAM_Gray", frame2)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()