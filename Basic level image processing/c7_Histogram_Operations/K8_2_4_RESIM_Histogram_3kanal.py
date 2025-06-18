



import cv2
import numpy as np
from matplotlib import pyplot as plt
  

img = cv2.imread('bee.jpg')
  

colors = ('b','g','r')


  
for i,color in enumerate(colors):
    hist = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color = color)
    
    
    
    
plt.title('Image Histogram')
plt.show()

cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
