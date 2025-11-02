#befejezni!!
class Node:                  # Csomópont osztály
    def __init__(self,data): # ez a speciális metódus a konstruktor
        self.data=data       # a self paraméter az osztály aktuális példányára való hivatkozás
        self.next=None       # a csomóponthoz tartozó adatot a data adattag tartalmazza
                             # a next adattag a következő csomópont címét tartalmazza, kezdetben
                             # "nem mutat sehova"
    def __str__(self):
        return str(self.data) # a csomópont sztringreprezentációja csak az adatrész
                              # sztringreprezentációja
    
class LinkedList:           # LáncoltLista osztály
    def __init__(self):     # konstruktor
        self.head=None      # a lista kezdetben üres, a fej "nem mutat sehova"

    def insertAtBeginning(self,data):   # ElejéreBeszúr művelet
        new_node=Node(data)             # új csomópont létrehozása a tárolandó adattal
        new_node.next=self.head         # az új csomópont után következik a teljes eddigi lista
        self.head=new_node              # az új csomópont lesz a lista új feje

    def printList(self):     # Bejár művelet; az összes adat kiírása
        tmp=self.head        # tmp a segédcsomópont, amely kezdetben a fej: innen indul a kiírás
        while tmp:           # egyenértékű: while tmp is not None, vagyis amíg nem érünk a végére
            print(tmp,end=" ")   
            tmp=tmp.next
        print()


#főprogram

szavak = LinkedList()

szavak.insertAtBeginning( "lehet")

print("Egyelemű lista:")
szavak.printList()

print()

szavak.insertAtBeginning("könnyű")

print("3-elemű lista:")




    

    

