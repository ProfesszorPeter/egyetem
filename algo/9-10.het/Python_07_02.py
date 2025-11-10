class Node:                     # Csomópont osztály
    def __init__(self, data):   # konstruktor
        self.data=data          # a csomóponthoz tartozó adat
        self.left=None          # balgyerek üres, "nem mutat sehova"
        self.right=None         # jobbgyerek üres, "nem mutat sehova"
                                # néha szoktak szülő mutatót is alkalmazni

    def __str__(self):
        return str(self.data)   # az adatrész sztringreprezenációját adja vissza

class BinaryTree:                 # BinFa, azaz bináris fa
    def __init__(self,data=None): # konstruktor
        if data==None:            # üres fa
            self.root=None        # a gyökérmutató (root) "nem mutat sehova"
        else:
            new_node=Node(data)   # a gyökércsomópont létrehozása (egyelemű fa)
            self.root=new_node    # a gyökérmutató a gyökércsomópontra mutat
        self.act=self.root        # kezdetben az aktuális (act) mutató a gyökérre mutat

    def isEmpty(self):            # Üres_e művelet
        return self.root==None    # ha a gyökér "nem mutat sehova", akkor a fa üres
    
    def Top(self):                # Elejére művelet
        self.act=self.root        # az act mutató a gyökérre mutasson

    def Next(self,direction): # Következőre műv.: iránytól függően léptetjük az act mutatót
        if self.act!=None:    # ha az act nem "sehova", vagyis létező csomópontra mutat,
            if direction=="balra":      # és ha az irány balra, akkor  
                self.act=self.act.left  # lépjünk a balgyerekre; 
            if direction=="jobbra":     # és ha az irány jobbra, akkor
                self.act=self.act.right # lépjünk a jobbgyerekre

    # BKJ-bejárás (bal-közép-jobb bejárás; inorder bejárás)
    def traversalInOrder(self):        # az aktuális objektum rekurzív InOrder fv.-ét hívja
        return self.InOrder(self.root) # meg a gyökércsomóponttal, amely listában adja vissza
                                       # a csomópontokban tárolt adatokat
    def InOrder(self,node):
        result=[]                          # a lista üresre állítása
        if node:                           # ha a csomópont nem üres, azaz van gyereke, akkor
            result=self.InOrder(node.left) # rekurzívan bejárjuk a bal részfát 
            result.append(node.data)       # az eredménylistához fűzzük a csomópont adatát
            result+=self.InOrder(node.right) # hozzáfűzzük a rekurzívan bejárt jobb részfát 
        return result                        # visszaadjuk a kész listát a bejárást indító
                                             # függvénynek


#főprogram
binfa=BinaryTree(14)
binfa.root.left=Node(19)
binfa.root.left.left=Node(23)
binfa.root.left.right=Node(6)
binfa.root.left.right.left=Node(10)
binfa.root.left.right.right=Node(21)
binfa.root.right=Node(15)
binfa.root.right.left=Node(3)
print("A bináris fa:\n");
print("       14");
print("      /  \\");
print("    19     15");
print("   / \     /");
print(" 23   6   3");
print("     /\\");
print("   10  21");
print()
items=binfa.traversalInOrder()
print("A bináris fa bal-közép-jobb (inorder) bejárása:\n")
for item in items:
    print(item,end=' ')
print("\n")
