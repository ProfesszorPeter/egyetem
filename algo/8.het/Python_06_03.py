# csak a képernyőtörlés miatt

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
              # a vég (farok) az utolsó elemre mutat, kezdetben "sehova"
              # az elemeket számolja, kezdetben 0
              # történt-e hiba valamelyik műveletnél
                            # (másik lehetőség: kivételkezeléssel) 

    def insertAtBeginning(self,data):   # ElejéreBeszúr művelet
        new_node=Node(data)             # új csomópont létrehozása a tárolandó adattal
        new_node.next=self.head         # az új csomópont után következik a teljes eddigi lista
        self.head=new_node              # az új csomópont lesz a lista új feje
                     # ha eddig üres volt a lista, akkor 
                     # a tail-t az új, egyetlen elemre kell állítani
                        # elemszám növelése 1-gyel
                        # nem történt hiba 

    def printList(self):      # Bejár művelet; az összes adat kiírása
        tmp=self.head         # tmp a segédcsomópont, amely kezdetben a fej: innen indul a kiírás
        while tmp:            # egyenértékű: while tmp is not None, vagyis amíg nem érünk a végére
            # adat kiírása
            tmp=tmp.next               # következő csomópontra lépés
            # ha nem az utolsó csomópont, akkor
            # kiíratunk utána egy nyilat; így az utolsó után nem lesz
        print()



#főprogram
# képernyőtörlés - ez így csak Windows alatt jó
szavak=LinkedList()
szavak.insertAtBeginning("lehet")
szavak.insertAtBeginning("könnyű")
szavak.insertAtBeginning("Neked")
print("A lista:")
szavak.printList()
print()



    

