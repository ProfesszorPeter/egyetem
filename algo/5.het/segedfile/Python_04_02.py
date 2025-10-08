import math

# Mohó algoritmus,


def erme_moho(ermek, osszeg):
    megoldas = []  # üres lista, melyben a felhasznált érméket tároljuk

    # Feladat! - érmevizsgálat
    for erme in ermek:
        print(f"osszeg {osszeg}, akt_ertek {erme}")
        if osszeg / erme >= 1:
            megoldas.append((erme, math.floor(osszeg / erme)))
            osszeg = osszeg % erme
            print(osszeg)

    return megoldas  # visszatérünk a megoldas listával


# A pénzérmék értékei csökkenő sorrendben
ermek = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
# Összeg, amit ki szeretnénk rakni az érmékből
osszeg = 2797
megoldas = erme_moho(ermek, osszeg)
print("A választott érmék értéke és darabszáma: ", megoldas)
