# -*- coding: utf-8 -*-
"""
Created on Thu May 25 21:49:58 2023

@author: MUOZIC
"""

import numpy as np
import cv2
from scipy.spatial import distance as dist
import math
import math, os
import imutils



img = cv2.imread('R1_BUGDAY_TEK_renkli.png')
img15 = cv2.imread('R1_BUGDAY_TEK_renkli.png')

# img = cv2.resize(img, (1450, 1250))
# img15 = cv2.resize(img15, (1450, 1250))

img_rectangle=img.copy()
img_centroid=img.copy()
img_circle=img.copy()
img_box=img.copy()
img_orta=img.copy()
img_ellipse=img.copy()
img_ellipse2=img.copy()
img_cevre=img.copy()
img_box2=img.copy()
img_Extreme_Points=img.copy()

gray2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=cv2.blur(gray2,(5,5))
_, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)



cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]

for contour in cnts:

    # ÇEVRE ÇİZİMİ
    img_cevre=img.copy()
    cv2.drawContours(img_cevre, [contour], 0, (0, 255, 255), 1)
    perimeter = cv2.arcLength(contour,True)
    print(perimeter)
    
    # SINIRLAYICI KUTU ÇİZİMİ
    img_rectangle=img.copy()
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(img_rectangle, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    img_rectangle2=img.copy()
    (x, y, w, h) = cv2.boundingRect(contour)
    cv2.rectangle(img_rectangle2, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.circle(img_rectangle2, (x,y), 8, (0, 255, 255), -1)
    cv2.putText(img_rectangle2, "(X:"+str(x)+","+"Y:"+str(y)+")" ,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
    cv2.putText(img_rectangle2, "w:"+str(w)+","+"h:"+str(h)+"" ,(x,y-60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)


    #ALAN BULMA
    area = cv2.contourArea(contour)
    print(area)
    
    
    # AĞIRLIK MERKEZİ BULMA
    img_centroid=img.copy()    
    M = cv2.moments(contour)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    Centroid = (int(cX),int(cY))
    cv2.circle(img_centroid, (cX, cY), 5, (0, 255, 255), -1)
    cv2.putText(img_centroid,"(cX:"+str(cX)+","+"cY:"+str(cY)+")" ,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)

    # MOMENT İLE ALAN
    print(M['m00'])
    
    
    
     # 5-Circle Çizdir
    img_circle=img.copy()
    (l, k), radius = cv2.minEnclosingCircle(contour)
    center = (int(l), int(k))
    radius = int(radius)
    cv2.circle(img_circle, center, radius, (0, 255, 0), 2)
    cv2.circle(img_circle,center,5,(0,255,255),3)
    cv2.line(img_circle, center, (center[0], center[1]+radius), (0,0,255), 2)
    cv2.line(img_circle, center, (center[0], center[1]-radius), (0,0,255), 2)
    cv2.line(img_circle, center, (center[0]+radius, center[1]), (0,0,255), 2)
    cv2.line(img_circle, center, (center[0]-radius, center[1]), (0,0,255), 2)
    cv2.putText(img_circle, "(X:"+str(l)+","+"Y:"+str(k)+")" ,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
    cv2.putText(img_circle, "Radius:"+str(radius) ,(x,y-60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
    
    # Aspect Ratio
    x,y,w,h = cv2.boundingRect(contour)
    aspect_ratio = float(w)/h
    print(aspect_ratio)
    
     #Extent
    area = cv2.contourArea(contour)
    x,y,w,h = cv2.boundingRect(contour)
    rect_area = w*h
    extent = float(area)/rect_area 
    print(extent)
    
    #Solidity
    area = cv2.contourArea(contour)
    hull = cv2.convexHull(contour)
    hull_area = cv2.contourArea(hull)
    solidity = float(area)/hull_area
    print(solidity)
    
    
      #Equivalent Diameter
    area = cv2.contourArea(contour)
    equi_diameter = np.sqrt(4*area/np.pi) 
    print(equi_diameter)
    
    # Ellipse
    
    img_ellipse=img.copy()
    ellipse = cv2.fitEllipse(contour)
    cv2.ellipse(img_ellipse,ellipse,(0,255,255),3)
    
    
    #Eccentricity
    (x,y),(MA,ma),angle = cv2.fitEllipse(contour) 
    
    a = ma/2
    b = MA/2
    
    eccentricity = math.sqrt(pow(a,2)-pow(b,2))
    eccentricity = round(eccentricity/a,2)
    print(eccentricity)
    
    
    ellipse = cv2.fitEllipse(contour)
    (xc,yc),(d1,d2),angle = ellipse
    #print(xc,yc,d1,d1,angle)

    # draw ellipse
    result = img.copy()
    cv2.ellipse(result, ellipse, (0, 255, 0), 3)
    # draw circle at center
    xc, yc = ellipse[0]
    cv2.circle(result, (int(xc),int(yc)), 10, (255, 255, 255), -1)

    # draw vertical line
    # compute major radius
    rmajor = max(d1,d2)/2
    if angle > 90:
        angle = angle - 90
    else:
        angle = angle + 90
    #print(angle)
    xtop = xc + math.cos(math.radians(angle))*rmajor
    ytop = yc + math.sin(math.radians(angle))*rmajor
    xbot = xc + math.cos(math.radians(angle+180))*rmajor
    ybot = yc + math.sin(math.radians(angle+180))*rmajor
    cv2.line(result, (int(xtop),int(ytop)), (int(xbot),int(ybot)), (0, 0, 255), 3)
    
    
    rmajor = min(d1,d2)/2
    if angle > 90:
        angle = angle - 90
    else:
        angle = angle + 90
    #print(angle)
    xtop = xc + math.cos(math.radians(angle))*rmajor
    ytop = yc + math.sin(math.radians(angle))*rmajor
    xbot = xc + math.cos(math.radians(angle+180))*rmajor
    ybot = yc + math.sin(math.radians(angle+180))*rmajor
    cv2.line(result, (int(xtop),int(ytop)), (int(xbot),int(ybot)), (0, 0, 255), 3)
    
    
    img_convex_hull=img.copy()

    
    hull = []
    
    for i in range(len(contour)):
        hull.append(cv2.convexHull(contour[i],False))
    
    bg = np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8)
    
    for i in range(len(contour)):
        cv2.drawContours(img_convex_hull,contour,i,(0,255,255),3,8)
        cv2.drawContours(img_convex_hull,hull,i,(0,255,255),1,8)

    

cv2.imshow("Renkli",img15)
cv2.imshow("Gray2",gray2)
cv2.imshow("thresh",thresh)
cv2.imshow("img_cevre",img_cevre)
cv2.imshow("img_rectangle",img_rectangle)
cv2.imshow("img_rectangle2",img_rectangle2)
cv2.imshow("img_centroid",img_centroid)
cv2.imshow("img_circle",img_circle)
cv2.imshow("img_ellipse",img_ellipse)
cv2.imshow("Ellips_Cizim",result)
cv2.imshow("img_convex_hull",img_convex_hull)

cv2.imwrite("Elips_BUGDAY_56_100s.png", thresh)
cv2.imwrite("Box_Elips_BUGDAY_56_100s.png", img_cevre)
cv2.imwrite("Circle_Elips_BUGDAY_56_100s.png", img_rectangle)
cv2.imwrite("Thresh_Elips_BUGDAY_56_100s.png", img_rectangle2)
cv2.imwrite("Cevre_BUGDAY_56_100s.png", img_centroid)
cv2.imwrite("Rectangle_BUGDAY_56_100s.png", img_circle)
cv2.imwrite("Extreme_BUGDAY_56_100s.png", img_ellipse)
cv2.imwrite("Sayac_BUGDAY_56_100s.png", result)



cv2.waitKey(0)
cv2.destroyAllWindows()