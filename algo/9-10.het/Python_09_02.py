import os
class Graph:
    def __init__(self,dict=None): # konstruktor
        if dict==None:            # ha nem adtunk meg dict, azaz szótár paramétert, akkor
            dict={}               # legyen üres, és így a gráf is üres;
        self.dict=dict            # a dict adattagba kerül a dict paraméter értéke

    def getVertices(self):              # Csúcsok művelet:
        return list(self.dict.keys())   # egy listában adja vissza a gráf összes csúcsát

    def getEdges(self, directed=True): # Élek művelet: ha a gráf nem irányított, akkor
        edges=[]                         # a directed paramétert False-nak kell megadni;
        for u in self.dict:              # egy listában adja vissza a gráf összes élét;
            for v in self.dict[u]:
                if directed:            # ha a gráf irányított: 
                    edges.append((u,v)) # akkor az (u,v) él mindenképpen bekerül a listába; 
                elif (v,u) not in edges:# különben (irányítatlan) ha fordított sorrendben 
                    edges.append((u,v)) # még nincs az éllistában, akkor felvesszük az 
        return edges                    # (u,v) élt; végül visszaadjuk az élek listáját

    def addEdge(self,u,v,directed=True): # HozzáadÉl művelet:
        self.dict[u].append(v)             # az (u,v) él hozzáadása; 
        if not directed:                   # ha irányítatlan a gráf, akkor a (v,u) élt is kell
            self.dict[v].append(u)                            
  
    def removeEdge(self,u,v,directed=True): # EltávolítÉl művelet:
        self.dict[u].remove(v)                # törli az (u,v) élt;
        if not directed:                      # ha irányítatlan a gráf:  
            self.dict[v].remove(u)            # akkor a (v,u) élt is töröljük

    def Neighbors(self,u):           # Szomszédok művelet: az összes olyan csúcs listáját
        return self.dict[u]          # adja, amelyhez vezet él u-ból

    def addVertex(self,u):                 # HozzáadCsúcs művelet:
        if u not in self.dict:             # ha még nincs a gráfban ez a csúcs:
            self.dict[u]=[]                # akkor felvesszük üres szomszédsági listával
                                           # (vagyis izolált pontként)

    def Size(self):                 # Méret művelet: hány csúcspont van
        return len(self.dict)
    
    def isEdge(self,u,v):           # VanÉl művelet: visszaadott logikai értékkel jelzi,
        return v in self.dict[u]    # hogy van-e (u,v) él a gráfban


# főprogram
os.system('cls')
szotar={
            "0" : ["1","2","3"],
            "1" : ["0","3"],
            "2" : ["0","5","6"],
            "3" : ["0","1","4","6"],
            "4" : ["3","6"],
            "5" : ["2"],
            "6" : ["2","3","4"]
       }
graf=Graph(szotar)
 # csúcspontok száma
print("A gráf csúcsai: ",graf.getVertices())
print("A gráf élei: ",graf.getEdges(False))
print("\nFelvesszük a 10-es izolált pontot.")
 # a 10-es csúcspont hozzáadása
print("A 10-es csúcspontnak nincsenek szomszédjai:")
 # a 10-es csúcspont szomszédai (üres lista lesz)
print("\nA 3-as csúcspont szomszédjai:")
print(graf.Neighbors("3"))
print("\nFelvesszük a gráfba a (10,5) élt.")
 # a (10,5) él hozzáadása
print("A gráf élei most: ",graf.getEdges(False))
 # ha a (0,3) él a gráfban:
print("\nTöröltük a gráfból a (0,3) élt.")
 # a (0,3) él törlése
else:
    print("A gráfnak a (0,3) nem éle.")
print("A gráf élei most: ",graf.getEdges(False))
 # ha a (3,1) él a gráfban
    print("A gráfnak a (3,1) éle.")
else:
    print("A gráfnak a (3,1) nem éle.")

