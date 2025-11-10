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

    
#főprogram
uresfa = BinaryTree()
# üres bináris fa létrehozása uresfa néven
if uresfa.isEmpty():
    print("\nEz a binfa üres.")
# fa nevű egyelemű fa, a gyökérelem az „alma” szót tartalmazza
fa = BinaryTree("alma")
if fa.isEmpty(): # ha üres a fa:
    print("Ez a binfa üres.")
else:# különben:
    print("Ez a binfa nem üres.")
print(fa.root)# gyökérelem kiírása
print(fa.act)# aktuális elem kiírása 
fa.root.left=Node("körte") # a gyökérelem balgyereke
fa.root.right = Node("banán")# a gyökérelem jobbgyereke tartalmazza a "banán" szót
print("A(z)",fa.root,"gyökérelem balgyereke:",fa.root.left)
fa.Next("jobbra")# léptessük jobbra az aktuális mutatót
print(fa.act)# aktuális elem kiírása
