def osszeg(*szamok):
    ossz = 0
    for szám in szamok:
        ossz = ossz+szám  # összegezzük a szamok értékeit az ossz változóba
    return ossz


# keressük meg a szintaktikai hibát
print(f"A számok összege: ", osszeg(1, 2, 3, 4))


def osszefuz(*szinek, sep="/"):
    # írjuk ki a szinek változó típusát
    print(f"A *szinek típusa: ", type(szinek))
    return sep.join(szinek)


print("Színek :", osszefuz("lila", "kek", "zold"))
print("Színek(,) :", osszefuz("lila", "kek", "zold", sep=","))


def szemely_adatok(**adatok):
    # írjuk ki az adatok változó típusát
    print(f"A **adatok típusa: ", type(adatok))
    for kulcs, ertek in adatok.items():
        print(f"{kulcs}: {ertek}")


szemely_adatok(név="Péter", életkor=30, varos="Budapest",
               szin="lila")  # szemely_adatok feltöltése értékekkel
