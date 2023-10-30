# Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

sayi = (int(input("Lütfen sayi giriniz : ")))
bolenlerSum = 0

# Sayının bölenlerini bulup topladık
for i in range(1, sayi+1):
    if sayi % i == 0:
        bolenlerSum += i

# Mükemmel sayı olup olmadığını kontrol ettik
if (sayi*2 == bolenlerSum):
    print("Bu sayı mükemmel sayıdır")
else:
    print("Bu sayı mükemmel sayı değildir.")