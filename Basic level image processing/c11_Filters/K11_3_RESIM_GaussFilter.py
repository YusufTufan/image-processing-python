import cv2

# Görüntüyü yükle
img_filter = cv2.imread("Resim2_Coklu_Bugday.png")

# Gauss filtresini uygula
blur_2 = cv2.GaussianBlur(img_filter, (15, 15), cv2.BORDER_DEFAULT)



# Orijinal ve Gauss filtreli görüntüleri göster
cv2.imshow("original", img_filter)
cv2.imshow("Gaussian Blur", blur_2)

# Kullanıcı bir tuşa basana kadar bekleyin
cv2.waitKey(0)
cv2.destroyAllWindows()


# cv2.GaussianBlur() fonksiyonunda kullanılabilen borderType (3. parametre) değerleri aşağıdaki gibidir:

# cv2.BORDER_DEFAULT: Genellikle OpenCV'nin kendi varsayılan kenar doldurma yöntemini kullanmayı tercih edilir.

# cv2.BORDER_CONSTANT: Kenar piksellerini belirli bir sabit değerle doldurur. 
# Bu sabit değer borderValue parametresiyle belirlenir.

# cv2.BORDER_REPLICATE: Kenar piksellerini çoğaltarak doldurur. 
# İç piksellerin değerlerini kullanarak kenar piksellerini doldurur.

# cv2.BORDER_REFLECT: Kenar piksellerini yansıtarak doldurur. 
# Kenar piksellerini yansıtarak görüntünün iç kısmından aldığı değerlerle doldurur.

# cv2.BORDER_WRAP: Kenar piksellerini sarma yoluyla doldurur. 
# Görüntünün bir tarafından alınan değerleri, diğer tarafın kenar piksellerini doldurmak için kullanır.

# cv2.BORDER_REFLECT_101: Kenar piksellerini içeriklerini yansıtarak doldurur. 
# BORDER_REFLECT ile benzerdir, ancak sınır değerleri 0 değil 1 birimlik bir hata ile yansıtılır.

# cv2.BORDER_TRANSPARENT: Kenar piksellerini saydam olarak işler. 
# Bu, çıktı görüntüsünün kenar piksellerini tamamen doldurmaz ve onları saydam yapar.

# Mean filter, gürültüyü azaltmak için kullanılabilir, ancak kenarları koruma konusunda 
# Gaussian blur kadar etkili değildir. Kenarlar, ortalama filtre uygulandığında bulanıklaşabilir veya kaybolabilir.