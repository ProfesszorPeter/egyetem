import Python_02_07_modul as sajatmodul # modul átnevezése, elemek elérés . után

eredmény = sajatmodul.összeadas(3, 5) # összeadás metódus hívása
print(eredmény)
# osztas metódus hívása 3,5 értékekkel, eredmeny kiírása
print(sajatmodul.osztas(3,5))

from Python_02_07_modul import * # modul minden elemét előtag nélkül használhatjuk

eredmény = kivonas(3,5)
print(eredmény)
# szorzas metódus hívása 3,5 értékekkel, eredmény kiírása

print(szorzas(3,5))
