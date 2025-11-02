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
        new_node=Node(data)
        if self.head==None:         # ha üres volt a lista, akkor
            self.head=new_node      # létrehozunk egy új fejet és véget (a most létrehozott
            self.tail=self.head     # csomópontra mutatnak)
        else:                       # ekkor nem üres a lista, ezért a vége után
            self.tail.next=new_node # kell fűzni az új elemet: a korábbi vég(csomópont) az 
            self.tail=new_node      # új csomópontra mutat, és az új csomópont lesz a lista vége
        self.counter+=1             # elemszám növelése 1-gyel
        self.error=False            # nem történt hiba

    def insertAtPosition(self,data,n): # HelyreBeszúr művelet: az n. pozícióra szúrja be az elemet
        new_node=Node(data)
        if self.head==None or n<=1:    # ha a lista üres vagy a pozíció legfeljebb 1, akkor az
             new_node.next=self.head   # első helyre szúrja be
             self.head=new_node
             if self.tail==None:       # ha eddig üres volt a lista, akkor
                 self.tail=self.head   # a tail-t az új, egyetlen elemre kell állítani
        else:                          # tmp a segédcsomópont (temporary:ideiglenes)
            tmp=self.head              # az i mutatja, hogy éppen hányadik pozícióra lehetne
            i=2                        # beszúrni, vagyis a tmp mindig az (i-1). csomópontra mutat
            while tmp.next and i<n:    # itt az n legalább 2 (és a listának van legalább 1 eleme)
                tmp=tmp.next
                i+=1
            new_node.next=tmp.next     # a ciklus végeztével a tmp után kell beilleszteni az újat
            tmp.next=new_node          # ha n>(lista elemszáma), akkor is jó: a végére illeszti
            if n>self.counter:
                self.tail=new_node
        self.counter+=1
        self.error=False

    def removeLastNode(self):          # UtolsótTöröl művelet
        if self.head==None:            # üres listából nem lehet elemet törölni
            self.error=True
        else:
            self.counter-=1            # itt csökkentjük az elemszámot, mert ha
            if self.counter==0:        # 1 elemű volt a lista, akkor a törlés után üres lista lesz
                self.head=None
                self.tail=None
            else:
                tmp=self.head
                while tmp.next!=self.tail: # a tmp a ciklus végén az utolsó előtti csomópont lesz
                    tmp=tmp.next    
                tmp.next=None
                self.tail=tmp
            self.error=False
            # esetleg gondoskodni kell a törölt csomópont memóriaterületének
            # felszabadításáról

    def removeFirstNode(self):
            # üres listából nem lehet elemet törölni,
            if self.head == None:
                self.error = True
            # ezért a hibát igazra állítjuk
            else:                           # ekkor a lista nem üres:
                self.head = self.head.next
                # a következő csomópont lesz az új fej (vagy None)
                # elemszám csökkentése
                self.counter -= 1
                if self.counter == 0:
                # ha üres lett a lista, akkor
                    self.tail = self.head
                    # a tail is None lesz
                # nem volt hiba
                self.error = False


    def printList(self):       # Bejár művelet; az összes adat kiírása
        tmp=self.head          # tmp a segédcsomópont, amely kezdetben a fej: innen indul a kiírás
        while tmp:             # egyenértékű: while tmp is not None, vagyis amíg nem érünk a végére
            print(tmp,end='')  # adat kiírása
            tmp=tmp.next       # következő csomópontra lépés
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

szavak.insertAtEnd("!")
print("Az új lista:")
szavak.printList()
print()

szavak.insertAtPosition("nagyon",2)
print("A még újabb lista:")
szavak.printList()
print()

print("Az első elem nélküli lista:")
szavak.removeFirstNode()
szavak.printList()
print()

