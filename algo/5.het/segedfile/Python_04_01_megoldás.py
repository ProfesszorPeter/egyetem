# targyak (egy lista, ahol minden elem egy tárgyat reprezentál, súly és érték párokkal)
# és kapacitas (a hátizsák maximális teherbírása).
def hatizsak_moho(targyak, kapacitas):
    # Minden tárgyhoz hozzáad egy új elemet, ami az érték / súly arányt jelenti.
    # Ez azért fontos, mert így tudjuk rangsorolni a tárgyakat, hogy először a
    # legértékesebbeket pakoljuk a táskába.
    for i in range(len(targyak)): # Tároljuk el a listában az érték/súly arányt is!
        targyak[i].append(targyak[i][1] / targyak[i][0])
    print("Érték/súly számítása után: ", targyak)

    # Rendezzük a listát a kiszámolt érték/súly arány szerint csökkenő sorrendbe!
    # A key=lambda x: x[2] rész azt jelenti, hogy a harmadik elem (az érték/súly arány)
    # alapján rendezi a listát.
    targyak.sort(reverse=True, key=lambda x: x[2])
    print("Csökkenő rendezettség érték/súly alapján: ", targyak)

    # Hátizsák feltöltése:
    # A kód végigiterál a rendezett tárgyakon.
    # Ha a tárgy súlya kisebb, mint a hátizsákban még maradt hely,
    # akkor a tárgyat hozzáadjuk a kivalasztott_targyak listához,
    # frissítjük a szabad kapacitást és a maximum értéket.
    kivalasztott_targyak = []
    max_ertek = 0
    for i in range(len(targyak)):
        # Ha belefér, tegyük bele!
        if kapacitas > targyak[i][0]:
            kivalasztott_targyak.append(targyak[i])
            kapacitas -= targyak[i][0]
            max_ertek += targyak[i][1]
    return max_ertek, kivalasztott_targyak

# Fő program, ahol megadjuk a bemeneti adatokat
# definiáljuk a bemeneti adatokat (tárgyak és kapacitás)
# és meghívjuk a hatizsak_moho függvényt.
targyak = [[5, 3],[5, 5],[3, 6]]
kapacitas = 9
max_ertek, kivasztott_targyak = hatizsak_moho(targyak, kapacitas)

# A függvény visszatérési értékeit kiírjuk a képernyőre
# Maximum érték és kiválasztott tárgyak
print("A legnagyobb elérhető érték: ", max_ertek)
print("A kiválasztott tárgyak: ", kivasztott_targyak)
