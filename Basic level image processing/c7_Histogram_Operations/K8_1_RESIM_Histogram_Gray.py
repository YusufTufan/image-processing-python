



import cv2
import numpy as np
from matplotlib import pyplot as plt
  
img = cv2.imread('Resim1_Dort_Nohut.png',0)

hist = cv2.calcHist([img],[0],None,[256],[0,256])

plt.plot(hist, color='b')
plt.title('Gri Seviye Histogram')
plt.show()

cv2.imshow("Gri Seviye", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
