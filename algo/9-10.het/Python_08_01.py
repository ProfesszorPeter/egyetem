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
 
#főprogram
print("")
# üres keresőfa kerfa néven
# "körte" elem beillesztése
# "alma" elem beillesztése
# "barack" elem beillesztése
# "cseresznye" elem beillesztése
print("Az elemek növekvő sorrendben:")
# kiíratás --> ábécé sorrend szerinti eredményt kapunk
print()
# "cseresznye" elem beillesztése
print("Nem került még egyszer beillesztésre a cseresznye, mert már van!")
# kiíratás
print()
