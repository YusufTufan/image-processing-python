import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Resim6_sudoku.JPG', 0)
# img = cv2.imread('Resim2_Coklu_Bugday.png', 0)
# img = cv2.imread('Resim1_Dort_Nohut.png', 0)
# img = cv2.imread('Resim4_gurultuluresim.JPG', 0)
# img = cv2.imread('Resim17_Bitewing1.jpg', 0)


img = cv2.medianBlur(img, 5)

# Basit thresholding (127)
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Adaptive thresholding (MEAN_C)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)

# Adaptive thresholding (GAUSSIAN_C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 10)

# Otsu thresholding
ret, th4 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

basliklar = ['Orjinal Resim', 'Basit Thresholding (127)', 'MEAN_C', 'GAUSSIAN_C', 'OTSU']
resimler = [img, th1, th2, th3, th4]

for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(resimler[i], 'gray')
    plt.title(basliklar[i])
    plt.xticks([]), plt.yticks([])

plt.show()


# cv2.ADAPTIVE_THRESH_MEAN_C yöntemi, bir pikselin eşik değerini hesaplarken o pikselin etrafındaki bir bölgenin ortalamasını alır. 
# Bu yöntem, ışık koşullarındaki değişikliklerle başa çıkmak için uygundur.

# cv2.ADAPTIVE_THRESH_GAUSSIAN_C yöntemi, bir pikselin eşik değerini hesaplarken o pikselin etrafındaki bir bölgenin ağırlıklı ortalamasını alır. 
# Bu ağırlıklı ortalama, bir Gauss dağılımı kullanılarak hesaplanır. Bu yöntem, ortalama yöntemi gibi, ışık koşullarındaki değişikliklerle başa çıkmak için uygundur, ancak daha yumuşak geçişler sağlar.

# Her iki yöntem de ayrıca, blockSize ve C parametrelerini alır:

# blockSize: Her piksel için eşik değerinin hesaplanmasında kullanılacak bölge boyutunu belirtir. 
# Bu bölge, pikselin etrafında bir kare ya da dikdörtgen şeklinde olabilir. Örneğin, blockSize=9 bir 9x9 piksel bölgeyi temsil eder.

# C: Hesaplanan ortalama ya da ağırlıklı ortalama değerine bu sabiti ekler. 
# Bu, eşik değerini ayarlamak için kullanılır. Pozitif bir değer, eşik değerini artırırken, negatif bir değer eşik değerini azaltır.


