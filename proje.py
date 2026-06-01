import random
import math
from datetime import datetime

ad = "Ahmed Zahid Karadeniz"
ucret = 649.99
sadakat = 28
aktif = True

hizmetler = ["Mobil Hat","Fiber","TV","Bulut","Mobil Uygulama"]

musteri = {
    "ad": ad,
    "ucret": ucret,
    "sadakat": sadakat,
    "aktif": aktif
}

if ucret > 500 or sadakat > 24:
    print("VIP Müşteri")
else:
    print("Standart Müşteri")

print(ad.upper())

id_no = "IST-2026-" + str(random.randint(1000,9999))
print(id_no)

musteriler = [
    {"ad":"Ahmet","ucret":150,"sadakat":3,"aktif":True},
    {"ad":"Mehmet","ucret":850,"sadakat":30,"aktif":True},
    {"ad":"Ayşe","ucret":120,"sadakat":2,"aktif":False},
    {"ad":"Fatma","ucret":400,"sadakat":10,"aktif":True},
    {"ad":"Can","ucret":90,"sadakat":1,"aktif":False}
]

def tutar_hesapla(ucret):
    return ucret * 1.20

print("Tarih:", datetime.now().strftime("%d/%m/%Y"))

for i in musteriler:
    toplam = math.ceil(tutar_hesapla(i["ucret"]))

    print(i["ad"], "-", toplam, "TL")

    if i["aktif"] == False:
        print("Kritik Risk")
    elif i["sadakat"] < 6:
        print("Yüksek Risk")
    else:
        print("Düşük Risk")

hizmetler2 = ["Mobil Hat","TV","TV","Fiber","Mobil Hat"]

print(set(hizmetler2))

paketler = ("Bronz","Silver","Gold")
print(paketler)
