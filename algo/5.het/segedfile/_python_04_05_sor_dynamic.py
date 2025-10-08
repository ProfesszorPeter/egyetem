class DynamicQueue: # a dinamikus sor adatstruktúra reprezentálása
    def __init__(self):
        self.queue = [] # inicializálunk egy üres listát, amely a sor elemeit fogja tárolni

    def __len__(self):
        # visszaadja a self.queue lista hosszát, ami a sorban lévő elemek számát jelenti
        return len(self.queue)

    # Ez a metódus hozzáad egy elemet a sor végéhez
    def enqueue(self, item):
        # A self.queue.append(item) hozzáfűzi az item elemet a self.queue listához
        self.queue.append(item)

    # a metódus eltávolítja és visszaadja a sor elejéről az első elemet
    def dequeue(self):
        # ellenőrzi, hogy a sor üres-e
        # Ha igen, kivételt dob, mivel nem lehet eltávolítani elemet egy üres sorból
        if not self.queue:
            raise Exception("Queue is empty")
        # Ha a sor nem üres, a self.queue.pop(0) eltávolítja és visszaadja a lista első elemét
        return self.queue.pop(0)

    # visszaadja a sor elejéről az első elemet anélkül, hogy eltávolítaná
    def peek(self):
        # ellenőrzi, hogy a sor üres-e
        # Ha igen, kivételt dob
        if not self.queue:
            raise Exception("Queue is empty")
        # Ha a sor nem üres, a self.queue[0] visszaadja a lista első elemét
        return self.queue[0]

    def is_empty(self): # ellenőrzi, hogy a sor üres-e.
        return len(self.queue) == 0  # True, ha a sor üres

    # speciális metódus - a print() függvénnyel kiírjuk a sor tartalmát
    def __str__(self):
        return str(self.queue) # visszaadja a self.queue lista szöveges reprezentációját


# Példa használat
dynamic_queue = DynamicQueue() # objektum létrehozása

dynamic_queue.enqueue(1) # elemeket adunk a sorhoz
dynamic_queue.enqueue(2)
dynamic_queue.enqueue(3)
dynamic_queue.enqueue(4)
dynamic_queue.enqueue(5)
print(dynamic_queue)  # [1, 2, 3, 4, 5] 

print(dynamic_queue.dequeue())  # 1 - elem eltávolítása
dynamic_queue.enqueue(6)
dynamic_queue.enqueue(7)

print(dynamic_queue.peek())  # 2 - első elem lekérdezése
print(dynamic_queue.dequeue())  # 2 
print(dynamic_queue.dequeue())  # 3
print(dynamic_queue)  # [4, 5, 6]

