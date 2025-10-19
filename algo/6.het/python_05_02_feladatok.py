gyumolcsok = {
    "papaya": 300,
    "kókuszdió": 250,
}
print("Gyümölcsök szótár: ", gyumolcsok)

# Kérj be egy gyümölcs nevét a felhasználótól, majd írd ki az árát, ha benne van!
gyumi = input("Adjon meg egy gyümölcsöt ")
if gyumi in gyumolcsok:
    print(f"Benne van a szótárban. Ára: {gyumolcsok.get(gyumi)}")
    #print("A gyümölcs ára: ", gyumolcsok.get(gyumi, "Nincs ilyen gyümölcs"))


# Adj hozzá egy új elemet (név és ár) az új szótárhoz, amit a felhasználó ír be!
uj_gyumi_nev = input("Adjon hozzá egy gyümölcsöt: ")
uj_gyumi_ar = int(input(f"Adja meg az {uj_gyumi_nev} árát: "))



# Nézd meg a gyumolcsok szótár változását!
print("Gyümölcsök szótár (módosított): ", gyumolcsok)

# Rendezd a szótárt kulcsok szerint csökkenő sorrendbe!
rendezett_gyumolcsok = dict(sorted(gyumolcsok.items(), reverse=True))

print("Rendezett gyümölcsök kulcs szerint csökkenő sorrendben:", rendezett_gyumolcsok)

tobb_gyumolcs = {
    "szőlő": 300,
    "barack": 250,
    "banán": 200,
    "citrom": 180,
    "ananász": 400,
}
# Két szótár egyesítése (tobb_gyumolcs és gyumolcs)
osszes_gyumolcs = gyumolcsok | tobb_gyumolcs

print("Összes gyümölcs:", osszes_gyumolcs)

# Rendezd a szótárat értékek szerint növekvő sorrendbe!
ertek_szerint = dict(sorted(osszes_gyumolcs.items(), key=lambda item: item[1]))


print("Rendezett gyümölcsök ár szerint: ", ertek_szerint)

# Fűzd össze a kulcsokat egy sztringgé a következő elválasztóval (--)
elvalaszto = " -- "
gyumolcsok_string = elvalaszto.join(ertek_szerint.keys())

print("Gyümölcsök összefűzve:", gyumolcsok_string)
