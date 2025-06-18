
import cv2

# Görüntüyü yükle
img_median = cv2.imread("rose.jpg")

# Median (medyan) filtresini uygula
blur_m = cv2.medianBlur(img_median, 5)

# Orijinal ve median filtreli görüntüleri göster
cv2.imshow("original", img_median)
cv2.imshow("Median Blur", blur_m)

# Kullanıcı bir tuşa basana kadar bekleyin
cv2.waitKey(0)
cv2.destroyAllWindows()
