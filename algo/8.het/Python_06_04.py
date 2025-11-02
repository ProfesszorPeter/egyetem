import os

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
        self.tail=None      # a vég (farok) az utolsó elemre mutat, kezdetben "sehova"
        self.counter=0      # az elemeket számolja, kezdetben 0
        self.error=False    # történt-e hiba valamelyik műveletnél
                            # (másik lehetőség: kivételkezeléssel) 

    def insertAtBeginning(self,data):   # ElejéreBeszúr művelet
        new_node=Node(data)             # új csomópont létrehozása a tárolandó adattal
        new_node.next=self.head         # az új csomópont után következik a teljes eddigi lista
        self.head=new_node              # az új csomópont lesz a lista új feje
        if self.tail==None:             # ha eddig üres volt a lista, akkor 
            self.tail=self.head         # a tail-t az új, egyetlen elemre kell állítani
        self.counter+=1                 # elemszám növelése 1-gyel
        self.error=False                # nem történt hiba

    def insertAtEnd(self,data):     # VégéreBeszúr művelet
        new_node=Node(data)         # új csomópont létrehozása a tárolandó adattal
        if self.head==None:         # ha üres volt a lista, akkor
            self.head=new_node      # létrehozunk egy új fejet és véget (a most létrehozott
            self.tail=self.head     # csomópontra mutatnak)
        else:                       # ekkor nem üres a lista, ezért a vége után
            self.tail.next=new_node # kell fűzni az új elemet: a korábbi vég(csomópont) az új 
            self.tail=new_node      # csomópontra mutat, és az új csomópont lesz a lista vége
        ++self.counter              # elemszám növelése 1-gyel
        self.error=False            # nem történt hiba

    def insertAtPosition(self,data,n): # HelyreBeszúr művelet: az n. pozícióra szúrja be az elemet
        new_node=Node(data)
        if self.head==None or n<=1:    # ha a lista üres vagy a pozíció legfeljebb 1, akkor az
             new_node.next=self.head   # első helyre szúrja be
             self.head=new_node
        else:                          # tmp a segédcsomópont (temporary:ideiglenes)
            tmp=self.head              # az i mutatja, hogy éppen hányadik pozícióra lehetne
            i=2                        # beszúrni, vagyis a tmp mindig az (i-1). csomópontra mutat
            while tmp.next and i<n:    # itt az n legalább 2 (és a listának van legalább 1 eleme)
                tmp=tmp.next
                i+=1
            new_node.next=tmp.next     # a ciklus végeztével a tmp után kell beilleszteni az újat
            tmp.next=new_node          # ha n>=(lista elemszáma+1), akkor is jó: a végére illeszti
        ++self.counter
        self.error=False

    def printList(self):      # Bejár művelet; az összes adat kiírása
        tmp=self.head         # tmp a segédcsomópont, amely kezdetben a fej: innen indul a kiírás
        while tmp:            # egyenértékű: while tmp is not None, vagyis amíg nem érünk a végére
            print(tmp,end='')   # adat kiírása
            tmp=tmp.next        # következő csomópontra lépés
            if tmp:                     # ha nem az utolsó csomópont, akkor
                print(" --> ",end='')   # kiíratunk utána egy nyilat; így az utolsó után nem lesz
        print()

#főprogram
os.system("cls")
szavak=LinkedList()
szavak.insertAtBeginning("lehet")
szavak.insertAtBeginning("könnyű")
szavak.insertAtBeginning("Neked")
print("A lista:")
szavak.printList()
print()

# a lista végére egy felkiáltójel beszúrása
szavak.insertAtEnd("!")
print("Az új lista:")
# lista kiíratása
szavak.printList()
print()

# a Neked szó után, vagyis a 2. pozícióra a nagyon szó beszúrása
szavak.insertAtPosition("nagyon",2)
print("A még újabb lista:")
# lista kiíratása
szavak.printList()
print()



    

