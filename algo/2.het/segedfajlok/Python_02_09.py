try:
    lista = [1, 2, 'három', 4, 'öt', 6]
    for i in lista:
        try:
            # aktuális elem (i) szorzása 10-el és eredményének kiírása
        except:
            continue
    # 6. index kiírása a lista-ból

except IndexError as e:
    print("Túlindexelés történt! -->", e)

print('Vége...')


