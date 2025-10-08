# Pythonban a listát tudjuk használni sorként és veremként is.
# Sor (Queue) beépített listával
queue = []

# Adjunk hozzá elemeket a sorhoz! (enqueue) - 1,2,3 értékeket
queue.append(1)
queue.append(2)
queue.append(3)
print("Sor:", queue)  # [1, 2, 3]

# Távolítsunk el egy elemet a sor elejéről! (pop)
dequeued_item = queue.pop(0)
print("Kivett elem:", dequeued_item)  # 1
print("A sor kivétel után:", queue)  # [2, 3]

# Írjuk ki az első elemet! (peek)
print("Első elem:", queue[0])

# Verem (Stack) beépített listával
stack = []

# Adjunk hozzá elemeket a veremhez (append) - 1,2,3
stack.append(1)
stack.append(2)
stack.append(3)
print("Verem:", stack)  # [1, 2, 3]

# Távolítsunk egy elemet a verem tetejéről (pop)
popped_item =stack.pop()
print("Kivett elem:", popped_item)  # 3
print("Verem kivétel után:", stack)  # [1, 2]

# Nézzük meg a verem legfelső elemét (peek)
print("Következő elem:", stack[-1])  # 2


