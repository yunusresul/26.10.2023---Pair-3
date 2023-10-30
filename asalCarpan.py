# Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız.

sayi = int(input("Sayı gir:"))

bolenler = []
asalOlmayan = []

# Sayının pozitif tam bölenlerini bulduk (1 hariç) ve "bolenler" dizisine ekledik
for i in range(2, sayi+1):
    kalan = sayi % i
    if kalan == 0:
        bolenler.append(i)

print(f"Sayının pozitif tam bölenleri: {bolenler}")

# Bölenler arasından asal olmayanları bulduk ve "asalOlmayan" dizisine ekledik
for i in bolenler:
    for n in range(2, i):
        if i % n == 0:
            asalOlmayan.append(i)
            break

# "asalOlmayan" dizisini "bolenler" dizisinden çıkardık ki "bolenler" dizisinde sadece asal olanlar kalsın
for j in asalOlmayan:
    bolenler.remove(j)

print(f"Sayının asal çarpanları: {bolenler}")