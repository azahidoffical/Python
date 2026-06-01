# Akıllı Müşteri Yönetim ve Analiz Sistemi (Telco Senaryosu)

## Proje Hakkında

Bu proje, Python Programlama dersi dönem ödevi kapsamında geliştirilmiştir. Amaç; Python dilinde öğrenilen temel programlama kavramlarını gerçek hayata yakın bir telekomünikasyon (Telco) senaryosu üzerinde uygulamaktır.

Projede müşteri bilgileri yönetilmekte, faturalar hesaplanmakta ve müşterilerin hizmeti bırakma (Churn) riskleri analiz edilmektedir.

---

## Kullanılan Konular

* Değişkenler ve Veri Tipleri
* Listeler (List)
* Sözlükler (Dictionary)
* Koşullu İfadeler (If-Else)
* String İşlemleri
* Random Kütüphanesi
* Fonksiyonlar
* Döngüler (For Loop)
* Math Kütüphanesi
* Datetime Kütüphanesi
* Set Veri Yapısı
* Tuple Veri Yapısı

---

## Proje Özellikleri

### 1. Müşteri Bilgileri Yönetimi

Her müşteri için:

* Ad Soyad
* Aylık Ücret
* Sadakat Süresi
* Aktiflik Durumu

bilgileri tutulmaktadır.

### 2. VIP Müşteri Analizi

Aşağıdaki şartlardan biri sağlanıyorsa müşteri VIP olarak değerlendirilmektedir:

* Aylık ücret > 500 TL
* Sadakat süresi > 24 ay

### 3. Müşteri ID Üretimi

Random kütüphanesi kullanılarak aşağıdaki formatta benzersiz müşteri numarası oluşturulmaktadır:

IST-2026-XXXX

### 4. Fatura Hesaplama

Fonksiyon kullanılarak aylık ücret üzerine %20 KDV eklenmektedir.

### 5. Churn Analizi

Müşterilerin hizmeti bırakma riski analiz edilmektedir.

Kurallar:

* Aktif olmayan müşteriler → Kritik Risk
* Sadakat süresi 6 aydan az ve aylık ücreti düşük olan müşteriler → Yüksek Risk
* Diğer müşteriler → Düşük Risk

### 6. Set Kullanımı

Tekrarlı hizmetler set yapısı kullanılarak benzersiz hale getirilmektedir.

---

## Kullanılan Kütüphaneler

```python
import random
import math
import datetime
```

---

## Çalıştırma

```bash
python python_odev.py
```

veya Google Colab ortamında çalıştırılabilir.

---

## Proje Dosyaları

* python_odev.py → Kaynak kodlar
* Rapor.pdf → Proje raporu
* README.md → Proje açıklamaları

---

## Geliştirici

Python Programlama Dönem Ödevi

2025-2026 Bahar Dönemi
