class StaticStack:
    def __init__(self, capacity):
        self.capacity = capacity # Beállítja a verem kapacitását (maximum tárolható elemek száma)
        # Létrehoz egy listát a verem elemeinek tárolására
        # A lista elemei kezdetben None értékkel inicializálódnak
        self.stack = [None] * capacity
        # A verem tetejét jelző index kezdeti értéke -1
        # Mivel a verem még üres, a tetejére mutató index -1-re van állítva
        self.top = -1

    def __len__(self):
        # a lista indexelése 0-tól kezdődik, ezért 1-et adunk hozzá,
        # hogy megkapjuk a veremben lévő elemek tényleges számát
        return self.top + 1

    def push(self, item):
        # Ellenőrzi, hogy a verem tele van-e
        if self.top == self.capacity - 1:
            raise Exception("Stack is full")
        self.top += 1
        self.stack[self.top] = item # hozzáadja az elemet a verem tetejére

    # eltávolítja és visszaadja az elemet a verem tetejéről (LIFO)
    def pop(self):
        if self.top == -1: # Ellenőrzi, hogy a verem üres-e
            raise Exception("Stack is empty")
        item = self.stack[self.top] # Lementi az eltávolítandó elemet egy változóba
        self.stack[self.top] = None # memóriahasználat optimalizálás
        self.top -= 1 # top-1, a verem új legfelső elemére mutat
        return item # Visszaadja az eltávolított elemet

    # megvizsgáljuk a verem tetején lévő elemet anélkül, hogy eltávolítanánk
    def peek(self):
        if self.top == -1:
            raise Exception("Stack is empty")
        return self.stack[self.top] # ha nem üres a verem tetején lévő értéket adja vissza

    def is_empty(self): # ha üres a verem akkor True értéket ad vissza
        return self.top == -1

    def __str__(self): # szöveges megjelenítés
        # Visszaadja a self.stack lista azon részét,
        # amely az aktuálisan használt elemeket tartalmazza (0-tól self.top-ig)
        return str(self.stack[:self.top + 1])


# Példa használat
static_stack = StaticStack(5) # létrehozás 5 elemmel
static_stack.push(1) # elemek hozzáadása
static_stack.push(2)
static_stack.push(3)
static_stack.push(4)
static_stack.push(5)
print(static_stack)  # [1, 2, 3, 4, 5]
print(static_stack.pop())  # 5 - eltávolítja a felső elemet
print(static_stack.peek())  # 4 - megnézi a felső elemet
static_stack.push(6) # elem hozzáadása, azután már kivételt dobna, többet nem enged
print(static_stack)  # [1, 2, 3, 4, 6]
static_stack.push(7) # hiba, kivételkezelés
print(static_stack)


