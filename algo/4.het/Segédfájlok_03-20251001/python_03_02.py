def reszhalmazok(lista):
    # Alapeset: üres lista esetén az egyetlen részhalmaz az üres halmaz
    # if üres listavizsgálat:
        # üres listával tér vissza
    if len(lista) == 0:
        return [[]]
    else:
        # A lista első elemét kiválasztjuk
        # elso = ?
        elso = lista[0]
        # A maradék lista összes részhalmaza
        # maradek_reszhalmazok = ? rekurziv hívás
        maradek_reszhalmazok = reszhalmazok(lista[1:])
        # Létrehozzuk az összes lehetséges részhalmazt
        kombinaciok = []
        for halmaz in maradek_reszhalmazok:
            kombinaciok.append(halmaz)
            kombinaciok.append([elso] + halmaz)
        return sorted(kombinaciok, key=len) # részhalmaz hossza alapján rendez

# Példa meghívás:
print(reszhalmazok([1, 2, 3]))

