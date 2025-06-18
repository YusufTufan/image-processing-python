import cv2

# Görüntüyü yükle
img_bilateral = cv2.imread("Resim13_Rontgen_Panoramik.jpg")

# Bilateral filtre uygula
blur_b = cv2.bilateralFilter(img_bilateral, 9, 75, 75)



# blur_b = cv2.bilateralFilter(img_bilateral, 9, sigmaColor=None, sigmaSpace=None)

# Eğer bu parametreler None olarak bırakılırsa, OpenCV varsayılan değerleri kullanacaktır. 
# Bu, filtrelemenin ne kadar agresif olacağını belirlemek için otomatik olarak hesaplanan değerleri kullanır. 
# Bu varsayılan değerler, genellikle belirli bir uygulamanın ihtiyaçlarına ve işlenen görüntünün özelliklerine bağlı olarak optimize edilmiştir.


# Orijinal ve filtrelenmiş görüntüleri göster
cv2.imshow("original", img_bilateral)
cv2.imshow("Bilateral Blur", blur_b)

# Kullanıcı bir tuşa basana kadar bekleyin
cv2.waitKey(0)
cv2.destroyAllWindows()


# d: Filtre boyutu. Bu parametre, filtrelemenin etkili olduğu piksellerin yarıçapını belirtir. 
# Örneğin, d=9, filtreleme işleminin 9 piksel uzaklıktaki piksellere etki edeceğini belirtir. 
# Filtre boyutu büyüdükçe, daha geniş bir alan etkilenir ve daha yumuşak bir görüntü elde edilir.

# sigmaColor: Renk benzerliği gauss filtresi için standart sapma değeri. 
# Bu parametre, filtreleme sırasında bir pikselin çevresindeki diğer piksellerin ne kadar benzer
# olması gerektiğini belirler. Daha büyük bir sigmaColor değeri, renk benzerliğinin daha fazla dikkate alınacağı anlamına gelir.

# sigmaSpace: Uzamsal benzerlik gauss filtresi için standart sapma değeri. 
# Bu parametre, filtrelemenin her bir pikselin çevresindeki diğer piksellerin ne kadar benzer olması gerektiğini belirler. 
# Daha büyük bir sigmaSpace değeri, filtreleme işleminin daha büyük bir alan üzerinde etkili olacağı anlamına gelir.

# Yani, 9, sigmaColor ve sigmaSpace değerleri, bilateral filtreleme işleminin boyutunu ve benzerlik kriterlerini belirler. 
# Bu değerlerin doğru seçimi, gürültünün azaltılması ve aynı zamanda kenarların korunması dengesini sağlamak için önemlidir.