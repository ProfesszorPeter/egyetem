szam = 5

def faktorialis_rekurziv(n):
    if n == 0:
        return 1
    return n* faktorialis_rekurziv(n-1)

print(f"a faktoriálás eredménye: {faktorialis_rekurziv(szam)}")

def faktorialis_dinamikus(n):
    eredmeny = []
    szorzat = 1
    for i in range(1,n+1):
        eredmeny.append(i)

    for i in (eredmeny):
        szorzat *= i
    return(szorzat)

print("fa faktoriálás eredménye: ",faktorialis_dinamikus(szam))

