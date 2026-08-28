import math


def toplam(x, y):
    return x + y


def cıkarma(x, y):
    return x - y


def carpım(x, y):
    return x * y


def bolum(x, y):
    return x / y


def us(x, y):
    if x < 0 and y % 1 != 0:
        print("HATALI GİRİŞ!")
        return
    return x ** y


def kok(x, y):
    if x < 0 and y % 2 == 0:
        print("HATALI GİRİŞ!")
        return
    if x < 0:
        return -((-x) ** (1 / y))
    return x ** (1 / y)


def hipotenus(x, y):
    h = x ** 2 + y ** 2
    return math.sqrt(h)


while True:

    islem = input("""1 - TOPLAMA
2 - ÇIKARMA
3 - ÇARPMA
4 - BÖLME
5 - ÜS ALMA
6 - KÖK ALMA
7 - HİPOTENÜS BULMA
8 - ÇIKIŞ
İşlem: """)

    if islem == "8":
        print("İyi günler")
        break

    elif "1" <= islem <= "7":
        try:
            x = float(input("İlk sayı: "))
            y = float(input("İkinci sayı: "))
        except ValueError:
            print("HATALI GİRİŞ!")
            continue

        if islem == "1":
            sonuc = toplam(x, y)

        elif islem == "2":
            sonuc = cıkarma(x, y)

        elif islem == "3":
            sonuc = carpım(x, y)

        elif islem == "4":
            try:
                sonuc = bolum(x, y)
            except ZeroDivisionError:
                print("HATALI GİRİŞ!")
                continue
        elif islem == "5":
            try:
                sonuc = us(x, y)
            except ZeroDivisionError:
                print("HATALI GİRİŞ!")
                continue

            if sonuc is None:
                continue

        elif islem == "6":
            try:
                sonuc = kok(x, y)
            except ZeroDivisionError:
                print("HATALI GİRİŞ!")
                continue
            if sonuc is None:
                continue
        elif islem == "7":
            if x <= 0 or y <= 0:
                print("HATALI GİRİŞ!")
                continue
            sonuc = hipotenus(x, y)

        print("Sonuç:", sonuc)

    else:
        print("HATALI SEÇİM!")