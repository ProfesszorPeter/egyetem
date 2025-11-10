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

    # KBJ-bejárás (közép-bal-jobb bejárás; preorder bejárás)
    def traversalPreOrder(self):        
        return self.PreOrder(self.root) 
                                       
    def PreOrder(self,node):
        result=[]                         
        if node:     
            result.append(node.data)      
            result+=self.PreOrder(node.left)
            result+=self.PreOrder(node.right) 
        return result
    
    # BJK-bejárás (bal-jobb-közép bejárás; postorder bejárás)
    def traversalPostOrder(self):        
        return self.PostOrder(self.root) 
                                       
    def PostOrder(self,node):
        result=[]                         
        if node:     
            result=self.PostOrder(node.left)
            result+=self.PostOrder(node.right) 
            result.append(node.data)
        return result

    def isEnd(self):                # Végén_e művelet
        return self.act==None
    
    def rootElement(self):          # Gyökérelem művelet
        if not self.isEmpty():  
            return self.root.data
        else:
            return None

    def actualElement(self):        # Aktelem művelet
        if self.act!=None:
            return self.act.data
        else:
            return None
        
    def updateRootElement(self,data): # GyökérMódosít művelet
        if not self.isEmpty():
            self.root.data=data

    def updateActualElement(self,data): # AktElemMódosít művelet
        if self.act!=None:
            self.act.data=data

    # binfa aktuális csomópontjához binfa részfát illeszt a megadott irányba
    def insertBinTree(self,bintree,direction):  
        if self.isEmpty():                # ha a binfa üres volt, akkor ez lesz a binfa
            self.root=bintree.root
            self.act=self.root
        else:
            if direction=="balra" and self.act.left==None:  # ha a balgyerek "üres"
                self.act.left=bintree.root
            if direction=="jobbra" and self.act.right==None: # ha a jobbgyerek "üres"
                self.act.right=bintree.root

    # binfa aktuális csomópontja "alól" leválaszt egy binfát
    def removeBinTree(self,bintree,direction):             # a bintree lesz a leválasztott binfa
        if bintree.root==None and self.act!=None:
                if direction=="balra":
                    bintree.root=self.act.left
                    self.act.left=None
                if direction=="jobbra":
                    bintree.root=self.act.right
                    self.act.right=None
                bintree.act=bintree.root

    # binfa aktuális csomópontja "alól" lemásol egy binfát (az eredetiben is megmarad)
    def partOfBinTree(self,bintree,direction):
        if bintree.root==None and self.act!=None:
                if direction=="balra":
                    bintree.root=self.act.left
                if direction=="jobbra":
                    bintree.root=self.act.right
                bintree.act=bintree.root

    def printBinTree(self):
        for item in self.traversalInOrder():
            print(item,end=' ')


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
print("A bináris fa BKJ-bejárása:")
binfa.printBinTree()
print()

# a gyökértől "lelépünk" balra
# megint "lelépünk" balra, a 23-hoz jutunk
print("\nAz akt mutató most erre mutat: ",binfa.act)
binfa.insertBinTree(BinaryTree(100),"jobbra") # jobbgyerekének beszúrjuk a 100-at
# balgyerekének az 1-et
print("A 100 jobbra és az 1 balra beillesztése után BKJ-bejárás:")
binfa.printBinTree()
print()
binfa.Top() # jó lenne egy Előzőre metódus, ami visszalép a 19-re, azaz a szülőcsomópontra
# a 19-re állunk ezzel
#üres binfa létrehozása
# leválasztjuk a 19-es csomópont jobbgyerekét
print("\nA leválasztott részfa:")
reszfa.printBinTree()
print("\nA maradék bináris fa:")
binfa.printBinTree()
# elejére (gyökérre) állunk
# a 15-ös az aktuális
# 15 jobbgyerekének beillesztjük a leválasztott részfát
print("\nA bővített bináris fa:")
binfa.printBinTree()                                                                            
print()