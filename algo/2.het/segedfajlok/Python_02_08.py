with open('adatok.txt', 'r', encoding="utf-8") as fajl_1:
    print("---------for ciklussal----------")
    for sor in fajl_1: # a fájl teljes tartalmának beolvasása FOR ciklussal
        print(sor.strip()) # sor értékének kiírása eltávolítva a white spaceket

with open('adatok.txt', 'r', encoding="utf-8") as fajl_2:
    print("--------while ciklussal----------")
    # sor változó kezdőérték (1. sor beolvasása a fájlból readline() metódussal)
    # a fájl teljes tartalmának beolvasása WHILE ciklussal
        # sor értékének kiírása eltávolítva a white spaceket
        # sor léptetése a következő sorra (újabb sor beolvasása)


