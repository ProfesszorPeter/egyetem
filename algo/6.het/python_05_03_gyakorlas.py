# Palindrom ellenőrzés rekurzívan, iteratívan és brute force elveket követve
# Palindrom (palindróma) az a szókapcsolat, ami visszafelé olvasva ugyanaz.
# (pl. Géza kék az ég. Indul a görög aludni.
def palindrom_rek(s):
    return


def palindrom_iterativ(s):
    return


def palindrom_bruteforce(s):
    s.lower()
    s_vissza = s[s::-1]


s = input("Kérek egy vizsgálandó kifejezést: ")
# Vegyük ki a stringből a szóközöket, pontot, és tegyük kisbetűssé!

print("A szóközök eltávolítása után, csupa kisbetűvel: ")
print("Palindrom (iterativ):")
print("Palindrom (rekurziv):")
print("Palindrom (brute force): ", palindrom_bruteforce(s))

