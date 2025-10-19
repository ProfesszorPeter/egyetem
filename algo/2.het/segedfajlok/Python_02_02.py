# Argumentumok - alapértelmezett értékek megadása
# Ha a függvényt argumentum nélkül hívjuk meg, akkor az alapértelmezett értéket használja
def sajat_fuggveny3(a = 3, b = 6):
    for x in range(1, a+1):
        for y in range(1, b+1):
            print(x*y, end="\t")
        print("\n")

print("\n-----Argumentumok - alapértelmezett értékek megadása: üres")
# paraméterek megadása nélkül hívjuk meg a függvényt
sajat_fuggveny3()
print("\n-----Argumentumok - alapértelmezett értékek megadása: 2")
# egy paraméterrel hívjuk meg a függvényt, értéke legyen 2
sajat_fuggveny3(2)
print("\n-----Argumentumok - alapértelmezett értékek megadása: 4,4")
# két 4-es paraméterrel is hívjuk meg a függvényt
sajat_fuggveny3(4,4)


