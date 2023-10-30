# Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

sayi = int(input("Tam sayı giriniz:"))

if sayi > 1:
    for i in range(2, sayi):
        kalan = sayi % i
        if kalan == 0:
            print("Asal değildir")
            break
    else:           # Buradaki else'i bir tab geri yazmamızın sebebi else'i döngüden bağımsız hale getirmek. Eğer bunu döngüden bağımsız hale getirmezsek for döngüsünün her dönüşünde "if" şartı sağlanmadığında "else" bloğuna girip her seferinde bize "Sayı asaldır" yazdıracaktır. Lakin bunu for'dan bağımsız yaptığımız zaman for döngüsü bitmişse ve if koşulu sağlanamamışsa "else" bloğu içine girecek ve bir kere "Sayı asaldır" yazacaktır. "for" döngüsü içerisinde "if" koşulu bir kere sağlandığında ise "else" bloğu etkisiz kalacaktır.
        print("Sayı asaldır")

else:
    print("Asal değildir")