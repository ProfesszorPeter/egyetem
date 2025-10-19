# Halmaz létrehozása hárommal osztható számok halmaza 21-ig.

harommal_oszthato = set()
for szam in range(0, 22):
    if szam % 3 == 0:
        harommal_oszthato.add(szam)

print("Hárommal osztható számok halmaza: ", harommal_oszthato)
harommal_oszthato.add(21)

print("Hárommal osztható számok halmaza: ")

neggyel_oszthato = {x for x in range(0, 22) if x % 4 == 0}
# Néggyel osztható számok halmazának létrehozása

print("Néggyel osztható számok halmaza: ", neggyel_oszthato)

# Hozz létre egy halmazt, ami tartalmazza a páros számokat 0-tól 20-ig!

paros = {x for x in range(0, 21) if x % 2 == 0}
print("Páros számok halmaza 20-ig: ", paros)

# Add hozzá a páros számokat tartalmazó halmazhoz a 22 számot is!
paros.add(22)

print("Páros számok halmaza 22-ig: ", paros)

# Ellenőrizd, hogy részhalmaza-e a néggyel osztható számok halmaza a páros számok halmazának!
if neggyel_oszthato.issubset(paros):
    print("részhalmaza")
else:
    print("nem részhalmaza")


# Készíts egy hattal osztható halmazt, majd tedd bele az annak megfelelő számokat!
# Tipp: páros és hárommal osztható számok metszete.
hattal_oszthato = paros & harommal_oszthato

print("Hattal osztható számok halmaza: ", harommal_oszthato)

unio = harommal_oszthato.union(neggyel_oszthato)
#unio = harommal_oszthato | neggyel_oszthato
# Írd ki a hárommal és néggyel osztható számok unióját!
print("Hárommal vagy néggyel osztható számok uniója:", unio)
