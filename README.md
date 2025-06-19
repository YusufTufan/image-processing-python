# 🧠 Image Processing with Python
 
Bu repo, Python kullanarak gerçekleştirilen **temel ve ileri düzey görüntü işleme uygulamalarını** barındıran kapsamlı bir kaynaktır. Eğitim, akademik çalışma, araştırma ya da bireysel projeler için kullanılabilir. Kodlar, anlaşılır ve modüler olacak şekilde yapılandırılmıştır.
---

## 🎯 Projenin Amacı

Bu projenin temel hedefleri:

- Görüntü işleme algoritmalarının Python dili ile uygulamalı olarak öğrenilmesini sağlamak
- OpenCV, NumPy, Matplotlib gibi popüler kütüphaneleri etkin biçimde kullanarak gerçek dünya problemlerine çözüm geliştirmek
- Yüz tanıma, kenar tespiti, filtreleme, histogram analizi, frekans dönüşümleri gibi görüntü işleme konularında örnekler sunmak
- Yapay zekâ ve makine öğrenmesi projeleri için ön işleme (preprocessing) adımlarında kullanılabilecek araçlar geliştirmek
---

## 🗂️ Klasör ve Dosya Yapısı

Aşağıda proje klasör yapısı ve içerikleri özetlenmiştir:

```

image-processing-python/
│
├── c1_Basic_Coordinate_Operations/ # Piksel okuma, yazma, koordinat işlemleri
├── c2_Drawing_writing_arithmetic_operations/# Çizim (çizgi, daire), metin yazma, toplama-çıkarma vb.
├── c3_Basic_WebCAM_Operations/ # Web kamerası ile temel işlemler
├── c4_Basic_Video_Operations/ # Video dosyaları ile çalışma
├── c5_Basic_External_Camera_Operations/ # Harici kamera işlemleri (USB vs.)
├── c6_ANDROID_Connection/ # Android cihaz bağlantısı
├── c7_Histogram_Operations/ # Histogram oluşturma, eşitleme vb.
├── c8_Thresholding/ # Sabit ve adaptif eşikleme işlemleri
├── c9_Bitwise_Operators/ # Bit düzeyinde işlemler (AND, OR, NOT, XOR)
├── c10_Color_Image_Processing/ # Renk uzayları, kanal işlemleri
├── c11_Filters/ # Filtreleme: Gaussian, Median, Mean
├── c12_Morphological_Operators/ # Dilation, erosion, opening, closing vb.
├── c13_Object_Properties/ # Nesne tespiti ve özellik çıkarımı
├── c14_MediaPipe/ # MediaPipe ile el, yüz, poz algılama
└── c15_other/ # Diğer veya yardımcı kodlar

````

---

## ⚙️ Gereksinimler ve Kurulum

### 🔧 Gereken Kütüphaneler

Projeyi çalıştırmak için aşağıdaki Python paketlerine ihtiyacınız olacak:

- `opencv-python`
- `numpy`
- `matplotlib`
- `deepface` (sadece yüz tanıma için)

Kurulum (pip ile):

```bash
pip install numpy opencv-python matplotlib deepface
````

Python 3.8 veya üzeri önerilmektedir.

---

## 🚀 Nasıl Kullanılır?

1. Reponun bir kopyasını yerel bilgisayarınıza klonlayın:

```bash
git clone https://github.com/YusufTufan/image-processing-python.git
cd image-processing-python
```

2. İlgilendiğiniz klasöre girin:

```bash
cd filtering
python gaussian_filter.py
```

3. Kodlar doğrudan `.py` uzantılı dosyalardan çalıştırılabilir. Kodlar içerisinde hem açıklamalar hem de çıktı örnekleri bulunmaktadır.

---

## 🧪 Örnek Konular

Projede yer alan başlıca örnekler:

| Konu                      | Açıklama                                 |
| ------------------------- | ---------------------------------------- |
| 📸 Yüz Tanıma             | DeepFace ile gerçek zamanlı yüz tanıma   |
| 🌈 Histogram Analizi      | Görüntü histogramı ve eşitleme           |
| 🎛️ Filtreleme Teknikleri | Gaussian, Median, Mean filtreler         |
| 🧾 Fourier Dönüşümü       | Görüntü frekans analizleri ve filtreleme |
| ⚫ Thresholding            | Sabit/adaptif eşikleme yöntemleri        |

---

## 📷 Görsel Örnekler (isteğe bağlı)

İlgili dosyalar çalıştırıldığında aşağıdaki gibi çıktılar elde edilir:

> 📌 Örnek görüntüler ve çıktı grafiklerini eklemek istiyorsan, `images/` klasörü oluşturulup burada `.png` olarak saklanabilir.

```python
# Örneğin: histogram_equalization.py
# Matplotlib ile önce ve sonra histogramı yan yana gösterebilir
```

---

## 🧩 Kullanılan Teknolojiler

* [Python 3](https://www.python.org/)
* [OpenCV](https://opencv.org/)
* [NumPy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)
* [DeepFace](https://github.com/serengil/deepface)

---
## 📄 Lisans
Bu proje MIT lisansı ile lisanslanmıştır. Detaylı bilgi için `LICENSE` dosyasına göz atabilirsiniz.
---

## ✍️ Hazırlayan

**Yusuf Tufan**
GitHub: [@YusufTufan](https://github.com/YusufTufan)
---

> Bu repo, yapay zekâ ve görüntü işleme yolculuğunuzda size güçlü bir temel sunmak üzere hazırlanmıştır.
