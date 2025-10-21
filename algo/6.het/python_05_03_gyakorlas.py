# Palindrom ellenőrzés rekurzívan, iteratívan és brute force elveket követve
# Palindrom (palindróma) az a szókapcsolat, ami visszafelé olvasva ugyanaz.
# (pl. Géza kék az ég. Indul a görög aludni.
def palindrom_rek(s):

    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return palindrom_rek(s[1:-1])


def palindrom_iterativ(s):
    eleje = 0
    vege = len(s) - 1

    while eleje != vege:
        if s[eleje] == s[vege]:
            eleje += 1
            vege -= 1
        else:
            return False

    return True


def palindrom_bruteforce(s):
    return s == s[::-1]


s = input("Kérek egy vizsgálandó kifejezést: ")
# Vegyük ki a stringből a szóközöket, pontot, és tegyük kisbetűssé!
s = s.replace(" ", "").lower().strip().replace(".", "")

print("A szóközök eltávolítása után, csupa kisbetűvel: ", s)
print("Palindrom (iterativ):", palindrom_iterativ(s))
print("Palindrom (rekurziv):", palindrom_rek(s))
print("Palindrom (brute force): ", palindrom_bruteforce(s))

