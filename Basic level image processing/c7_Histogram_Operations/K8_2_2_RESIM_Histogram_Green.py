


import cv2
import numpy as np
from matplotlib import pyplot as plt
  
img = cv2.imread('bee.jpg')
  
hist = cv2.calcHist([img],[1],None,[256],[0,256])
  
plt.plot(hist, color='g')
plt.title('Yeşil Kanal')
plt.show()

cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()