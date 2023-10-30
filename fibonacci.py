# İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

dizi = [1, 1]

for i in range(18):
    dizi.append(dizi[len(dizi)-1] + dizi[len(dizi)-2])

print(dizi)