class Node:                     # Csomópont osztály
    def __init__(self, data):   # konstruktor
        self.data=data          # a csomóponthoz tartozó adat
        self.left=None          # balgyerek üres, "nem mutat sehova"
        self.right=None         # jobbgyerek üres, "nem mutat sehova"

    def __str__(self):
        return str(self.data)   # az adatrész sztringreprezenációját adja vissza

class BinarySearchTree:         # BinKerFa, azaz bináris keresőfa
    def __init__(self):         # konstruktor
        self.root=None          # a gyökérmutató (root) "nem mutat sehova"

    # BKJ-bejárás (bal-közép-jobb bejárás; inorder bejárás):
    # ennek hatására a kulcs szerinti rendezettséggel járjuk be a fát, vagyis
    # rendezetten írathatjuk ki az adatelemeket.
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

    def printBinTree(self):
        for item in self.traversalInOrder():
            print(item,end=' ')

    def Insert(self,data):    # Beilleszt művelet; a rendezettség szerinti helyére illeszti az elemet
        if self.root==None:       # ha üres volt a fa, akkor
            self.root=Node(data)  #  az új elemet gyökérként adjuk hozzá
        else:                                       # különben:
            self.recursiveInsert(self.root,data)    # a rekurzív fv. hívása a gyökércsomóponttal és a
                                                    # a beillesztendő adatelemmel (ami most kulcs is)

    def recursiveInsert(self,node,data):
        if data<node.data: # ha a beillesztendő elem kisebb, mint az aktuális csomópontbeli elem, akkor
            if node.left==None:        # ha az aktuális balgyereke üres, akkor 
                node.left=Node(data)   # ide tesszük az új elemet (és a rekurzió leáll)

            else:                      # különben (ekkor a balgyerek nem üres):
                self.recursiveInsert(node.left,data) # rekurzív hívással a bal oldali részfában folytatjuk
        else:                       # különben:
            if data>node.data: # ha a beillesztendő elem nagyobb, mint az aktuális csomópontbeli, akkor
                if node.right==None:   # ha az aktuális jobbgyereke üres, akkor 
                    node.right=Node(data) # ide tesszük az új elemet (és a rekurzió leáll)
                else:                     # különben (ekkor a jobbgyerek nem üres):
                    self.recursiveInsert(node.right,data) # rekurzív hívással a jobb oldali részfában
                                                          # folytatjuk
            # ha az "alulról második" if feltétele sem teljesül, akkor már van ilyen kulcsú elem 
 
    def traversalReverseOrder(self):        # az aktuális objektum rekurzív ReverseOrder fv.-ét hívja
        return self.ReverseOrder(self.root) # meg a gyökércsomóponttal, amely listában adja vissza
                                            # a csomópontokban tárolt adatokat
    def ReverseOrder(self,node):
        result=[]                          # a lista üresre állítása
        if node:                           # ha a csomópont nem üres, azaz van gyereke, akkor
            result=self.ReverseOrder(node.right) # rekurzívan bejárjuk a jobb részfát 
            result.append(node.data)             # az eredménylistához fűzzük a csomópont adatát
            result+=self.ReverseOrder(node.left) # hozzáfűzzük a rekurzívan bejárt bal részfát 
        return result                    # visszaadjuk a kész listát a bejárást indító függvénynek

    def Search(self,data):          # Keres művelet
        return self.recursiveSearch(self.root,data)  # a rekurzív függvény hívása
    
    def recursiveSearch(self,node,data):
        if node==None or node.data==data: # leállási feltétel (alapeset): a csomópont üres,
                                          # vagyis "leléptünk a fáról", azaz nincs a keresett elem;
                                          # vagy megtaláltuk
            return node
        if data<node.data:      # ha a keresett elem kisebb, mint a csomópontbeli, akkor
            return self.recursiveSearch(node.left,data) # a bal részfában folytatjuk a keresést
        return self.recursiveSearch(node.right,data) # a jobb részfában folytatjuk a keresést,
                                                     # mert itt csak data>node.data lehet már


#főprogram
kerfa=BinarySearchTree()
kerfa.Insert("körte")
kerfa.Insert("alma")
kerfa.Insert("barack")
kerfa.Insert("cseresznye")
print("Az elemek növekvő sorrendben:")
kerfa.printBinTree()
print()
kerfa.Insert("cseresznye")
print("Nem került még egyszer beillesztésre a cseresznye, mert már van!")
kerfa.printBinTree()
print()
if kerfa.Search("barack"): # barack keresése



# szilva keresése



# banán beillesztése
# szilva beillesztése
# ananász beillesztése
# fa bejárása
print()
# így is lehet: a visszaadott csomópont kerüljön a keresett nevű változóba
if keresett==None:      
    print("Nem tartalmazza a szilva-t.")
else:
    print("Tartalmazza a",keresett,"-t.")