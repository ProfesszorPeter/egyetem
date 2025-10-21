# 1. rész - Írj egy programot, ami verem segítségével ellenőrzi, hogy
# a felhasználó által beírt szövegben minden zárójelnek van-e párja!
# Például:
# Be: (()((())()))    Ki: helyes
# Be: ()((())         Ki: helytelen

s = input("Kérem a zárójelezést (): ") # pl (()((())()))
stack = []

print("Helyes vagy Helytelen")

# 2. rész - Írd meg úgy a programot, hogy a szögletes zárójeleket is figyelje!
# Be: (()[([])()])    Ki: helyes
# Be: ()[(]]          Ki: helytelen

s = input("Kérem a zárójelezést ([]): ") # pl (()[([])()])
stack = []


print("Helyes vagy Helytelen")
