products = {"apple": 3, "banana": 5, "bread": 2, "milk": 4}

urun1 = input("1. ürün: ")
urun2 = input("2. ürün: ")
urun3 = input("3. ürün: ")

sepet = [urun1, urun2, urun3]

toplam = 0
for urun in sepet:
    if urun in products:
        fiyat = products[urun]
        toplam = toplam + fiyat
    else:
        print(f"Uyarı: {urun} ürünü listede yok!")

print(f"Your basket: {urun1}, {urun2}, {urun3}")
print(f"Total price: {toplam} TL")