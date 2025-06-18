



import cv2

# Görüntüyü yükle
img_filter = cv2.imread("Resim1_Dort_Nohut.png")

# Mean (ortalama) filtresini uygula
blur = cv2.blur(img_filter, (11, 11))  # (7, 7) boyutlu bir filtre kullanılıyor

# Orijinal ve filtrelenmiş görüntüleri göster
cv2.imshow("original", img_filter)
cv2.imshow("blur", blur)

# Pencereyi kapatmak için bir tuşa basın
cv2.waitKey(0)
cv2.destroyAllWindows()
