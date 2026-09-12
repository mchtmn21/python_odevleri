cumle = input("Bir cümle yazın: ")

kelime = cumle.split()
print(kelime)
print(len(kelime))

cumle_bosluk = cumle.replace(" ", "")
print(len(cumle_bosluk))

benzersiz = set(kelime)
print(benzersiz)
print(len(benzersiz))

en_uzun = ""
for k in kelime:
    if len(k) > len(en_uzun):
        en_uzun = k
print(en_uzun)