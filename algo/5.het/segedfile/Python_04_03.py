# Hozz létre egy listát a kedvenc gyümölcseiddel!
from collections import Counter
gyumolcsok = ["alma", "körte", "szilva", "szőlő", "eper"]

# Kérj be egy gyümölcs nevét a felhasználótól, és ellenőrizd, hogy benne van-e a listában!
gyumi = input("Írj be egy gyümölcsnevet: ")
benne_van = False
if gyumi in gyumolcsok:
    benne_van = True
print("Benne van." if benne_van else "Nincs benne.")

# Másold le a listát egy másik listába!
gyumolcsok_masol = gyumolcsok[:]
# Adj hozzá egy elemet az új listához, amit a felhasználó ír be! Nézd meg, változott-e az eredeti lista!
gyumolcsok_masol.append(gyumi)
if gyumolcsok is gyumolcsok_masol:
    print("nem változott")
else:
    print("változott")
# Hogy lehet elérni, hogy az eredeti lista változzon/ne változzon?

# Rendezd a listát aszerint csökkenő sorrendbe, hogy hányszor szerepel benne az a betű!


def szamlal(gyumolcs):
    return Counter(gyumolcs)["a"]


gyumolcsok.sort(key=szamlal, reverse=True)
print(gyumolcsok)

# Készíts egy listát, ami tartalmazza a gyümölcs lista és az alábbi lista metszetét!
tobb_gyumolcs = ["szőlő", "barack", "alma", "banán", "cseresznye", "citrom", "ananász", "szilva"]

# Fűzd össze a két listát!
metszet = list(set(gyumolcsok) & set(tobb_gyumolcs))
print("Metszet: ", metszet)

# Összefűzés
osszefuzott = gyumolcsok + tobb_gyumolcs
print("összfűzott lista: ", osszefuzott)

# Távolítsd el a listából a duplikált elemeket!
osszefuzott = list(set(osszefuzott))

# Rendezd a listát, majd fűzd össze egy sztringggé a következő elválasztóval.
osszefuzott.sort()
koz = " -- "
osszefuzott_string = koz.join(osszefuzott)
print(osszefuzott_string)


