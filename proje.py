import random          # Kütüphane
import math            # Kütüphane
import datetime        # Kütüphane

print("AKILLI MÜŞTERİ YÖNETİM VE ANALİZ SİSTEMİ")

# 1. KISIM - Veri Yapıları ve Temel Mantık

ad_soyad = "Ahmed Zahid Karadeniz"      # String
aylik_ucret = 649.99                    # Float
sadakat_ayi = 28                        # Integer
aktif_mi = True                         # Boolean

hizmetler = [                           # Liste
    "Mobil Hat",
    "Fiber İnternet",
    "TV Paketi",
    "Bulut Depolama",
    "Mobil Uygulama"
]

musteri = {                             # Dictionary
    "ad_soyad": ad_soyad,
    "aylik_ucret": aylik_ucret,
    "sadakat_ayi": sadakat_ayi,
    "aktif_mi": aktif_mi,
    "hizmetler": hizmetler
}

if aylik_ucret > 500 or sadakat_ayi > 24:   # If-Else
    print("VIP Müşteri: İndirim Tanımla")
else:
    print("Standart Müşteri")

buyuk_ad = ad_soyad.upper()             # String İşlemi
customerID = "IST-2026-" + str(random.randint(1000, 9999))   # Random

print("Müşteri Adı:", buyuk_ad)
print("Customer ID:", customerID)
print("Müşteri Bilgileri:", musteri)

# 2. KISIM - Fonksiyonlar ve Döngüler

musteriler_listesi = [                  # Liste + Dictionary
    {"ad": "Ali", "aylik_ucret": 150, "sadakat_ayi": 3, "aktif": True},
    {"ad": "Ayşe", "aylik_ucret": 850, "sadakat_ayi": 30, "aktif": True},
    {"ad": "Mehmet", "aylik_ucret": 120, "sadakat_ayi": 2, "aktif": False},
    {"ad": "Zeynep", "aylik_ucret": 400, "sadakat_ayi": 10, "aktif": True},
    {"ad": "Can", "aylik_ucret": 90, "sadakat_ayi": 1, "aktif": False}
]

def tutar_hesapla(aylik_ucret):         # Fonksiyon
    return aylik_ucret * 1.20

bugun = datetime.datetime.now()         # Datetime

print("\nTELCO FATURA RAPORU")
print("Tarih:", bugun.strftime("%d-%m-%Y"))

for musteri in musteriler_listesi:      # For Döngüsü
    toplam = tutar_hesapla(musteri["aylik_ucret"])
    yuvarli_tutar = math.ceil(toplam)   # Math

    print("\nMüşteri:", musteri["ad"])
    print("Aylık Ücret:", musteri["aylik_ucret"])
    print("KDV Dahil:", yuvarli_tutar)

    if musteri["aktif"] == False:       # Churn Kontrol
        print("CHURN RİSKİ: KRİTİK")
    elif musteri["sadakat_ayi"] < 6 and musteri["aylik_ucret"] < 200:
        print("CHURN RİSKİ: YÜKSEK")
    else:
        print("CHURN RİSKİ: DÜŞÜK")

tum_hizmetler = [                       # Tekrarlı Liste
    "Mobil Hat",
    "Fiber İnternet",
    "TV Paketi",
    "Mobil Hat",
    "Bulut Depolama",
    "TV Paketi"
]

benzersiz_hizmetler = set(tum_hizmetler)   # Set

print("\nBenzersiz Hizmetler:", benzersiz_hizmetler)

sabit_paketler = ("Bronz", "Silver", "Gold")   # Tuple
print("Paketler:", sabit_paketler)