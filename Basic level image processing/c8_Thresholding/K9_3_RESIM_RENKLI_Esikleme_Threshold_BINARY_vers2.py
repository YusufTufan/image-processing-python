# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 02:40:05 2024

@author: muozi
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Renkli görüntüyü oku
img = cv2.imread('Resim2_Coklu_Bugday.png')

# Eşikleme işlemi uygula (cv2.THRESH_BINARY)
# Piksel değerleri eşik değerinden büyükse, 255 (beyaz) değerini alır, aksi halde 0 (siyah) değerini alır.
# renkli bir görüntü verildiğinde her bir kanal üzerinde ayrı ayrı eşikleme işlemi yapar. 
# Örneğin, bir RGB renkli görüntü verildiğinde, bu işlev her bir kanal için ayrı ayrı eşikleme işlemi yapar 
# ve sonuç olarak her bir kanalda ayrı bir eşiklenmiş görüntü elde eder. Daha sonra, bu eşiklenmiş görüntüler 
# birleştirilerek renkli bir görüntü elde edilir. Bu şekilde, her bir kanalın eşiklenmiş hali korunur ve 
# renkli görüntünün genel yapısı bozulmaz.

# KULLANIŞLI BİR YAKLAŞIM DEĞİLDİR VE GENEL OLARAK KULLANILMAZ. GORUNTU GRİ SEVİYEYE ÇEKİLMELİDİR
ret1, thresh1 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

# Gri seviye resmin histogramını hesapla
#eğer renkli bir görüntü verilirse, bu işlev otomatik olarak görüntüyü gri seviyeye dönüştürüp 
# histogramı gri tonlamalı görüntü üzerinde hesaplar. Yani, renkli bir görüntü verildiğinde bile, 
# bu kod gri seviye histogramı çıkaracaktır.
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Histogramı çiz
plt.plot(hist, color='b')
plt.title('Renkli Resim Histogramı')
plt.show()

# Resimleri göster
cv2.imshow("RENKLI", img)
cv2.imshow("THRESH_BINARY", thresh1)

# Bekle ve ekrandan çık
cv2.waitKey(0)
cv2.destroyAllWindows() 

