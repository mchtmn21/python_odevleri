import json
import csv
import os

DOSYA_ADI = "data/library.json"

# --- Program başlarken dosyayı güvenli şekilde oku ---
if os.path.exists(DOSYA_ADI):
    try:
        with open(DOSYA_ADI, "r") as f:
            kitaplar = json.load(f)
    except json.JSONDecodeError:
        print("Uyarı: library.json bozuk, boş kütüphaneyle başlanıyor.")
        kitaplar = []
else:
    print("İlk çalıştırma: library.json henüz yok, boş kütüphane oluşturuluyor.")
    kitaplar = []


def kaydet():
    """Kütüphaneyi diske yazar."""
    os.makedirs(os.path.dirname(DOSYA_ADI), exist_ok=True)
    with open(DOSYA_ADI, "w") as f:
        json.dump(kitaplar, f, indent=4)


while True:
    print("""
            1. Kitap ekle
            2. Tüm kitaplari görüntüle
            3. Kitap ara
            4. Kitap sil
            5. CSV'ye aktar
            6. CSV'den içe aktar
            7. Exit
            """)

    # --- Menü seçimini güvenli şekilde al ---
    try:
        secim = int(input("bir secim yap: "))
    except ValueError:
        print("Lütfen sadece sayı gir (1-7).")
        continue

    if secim == 1:
        kitap_adi = input("Title: ")
        yazar = input("Author: ")

        # --- Yıl doğrulaması: sayı olmayan girişte tekrar sor ---
        while True:
            try:
                yil = int(input("Year: "))
                break
            except ValueError:
                print("Yıl sadece rakamlardan oluşmalı, tekrar dene.")

        tur = input("Genre: ")
        kitaplar.append({"title": kitap_adi, "author": yazar, "year": yil, "genre": tur})
        kaydet()
        print("Kitap eklendi ve kaydedildi!")

    elif secim == 2:
        if not kitaplar:
            print("Kütüphanede henüz hiç kitap yok.")
        else:
            print(f"\n--- Kütüphaneniz ({len(kitaplar)} kitap) ---")
            for kitap in kitaplar:
                print(f"{kitap['title']:<20} {kitap['author']:<20} {kitap['year']:<6} {kitap['genre']}")
    elif secim == 3:
        arama = input("Aranacak kelime (title veya author): ").lower()
        sonuclar = [k for k in kitaplar if arama in k["title"].lower() or arama in k["author"].lower()]

        if not sonuclar:
            print("Eşleşen kitap bulunamadı.")
        else:
            print(f"\n--- {len(sonuclar)} sonuç bulundu ---")
            for kitap in sonuclar:
                print(f"{kitap['title']:<20} {kitap['author']:<20} {kitap['year']:<6} {kitap['genre']}")
    elif secim == 4:
        silinecek = input("Silinecek kitabın başlığı: ")
        bulundu = False
        for kitap in kitaplar:
            if kitap["title"].lower() == silinecek.lower():
                kitaplar.remove(kitap)
                bulundu = True
                break

        if bulundu:
            kaydet()
            print("Kitap silindi ve kaydedildi!")
        else:
            print("Bu başlıkta bir kitap bulunamadı.")
    elif secim == 5:
        "csv den dışa aktar"
    elif secim == 6:
        "csv den içe aktar"
    elif secim == 7:
        break
    else:
        print("Geçersiz seçim, 1-7 arası bir sayı gir.")
