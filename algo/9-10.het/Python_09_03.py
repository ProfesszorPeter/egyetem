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

    def Neighbors(self,u):          # Szomszédok művelet: az összes olyan csúcs listáját
        return self.dict.get(u)         # adja, amelyhez vezet él u-ból

    def addVertex(self,u):                 # HozzáadCsúcs művelet:
        if u not in self.dict:             # ha még nincs a gráfban ez a csúcs:
            self.dict[u]=[]                # akkor felvesszük üres szomszédsági listával
                                           # (vagyis izolált pontként)

    def Size(self):                 # Méret művelet: hány csúcspont van
        return len(self.dict)
    
    def isEdge(self,u,v):           # VanÉl művelet: visszaadott logikai értékkel jelzi,
        return v in self.dict[u]    # hogy van-e (u,v) él a gráfban


    def BreadthFirstTraversal(self,start): # SzélességiBejárás; nem rekurzív megvalósítás;
                                           # egy összefüggő gráfot tud csak bejárni 
        queue=[start]    # a kezdőpontot betesszük egy üres sorba (Python-lista sorként kezelve)
        visited=set()    # üreshalmaz létrehozása
        visited.add(start) # a kezdőpontot a halmazba is betesszük
                         # A sorba azon pontokat tesszük, amelyeket elért a bejárásunk, de még
                         # nem kerültek feldolgozásra.
                         # A halmazt arra használjuk, hogy egy elért ("meglátogatott") pontot,
                         # azaz vagy már feldolgozott, vagy feldolgozásra "kijelölt"
                         # (sorba bekerült) pontot ne vegyünk fel újból a sorba.
        while queue:     # egyenértékű ezzel: len(queue)!= 0, vagyis amíg nem üres a sor, addig: 
            node=queue.pop(0)     # kivesszük a sor elejéről a következő pontot a node-ba,
            print(node,end=' ')   # feldolgozzuk (azaz most kiírjuk), majd       
            for tmp in self.Neighbors(node):# az összes szomszédját megvizsgáljuk:   
                if tmp not in visited:      # ha a tmp szomszéd még nincs a halmazban: 
                    queue.append(tmp)       # akkor betesszük a sor végére és
                    visited.add(tmp)        # betesszük a halmazba is


    def rec_BreadthFirst(self,start,visited=None,queue=None):
        if visited is None:
            visited=set()
        if queue is None:
            queue=[start]
        if not queue:               # ha a sor üres, akkor visszatérés 
            return
        node=queue.pop(0)
        if node not in visited:
            print(node,end=' ')
            visited.add(node)
            for tmp in self.Neighbors(node):
                if tmp not in visited:
                    queue.append(tmp)
        self.rec_BreadthFirst(start,visited,queue)


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
print("A gráf csúcsai: ",graf.getVertices())
print("A gráf élei: ",graf.getEdges(False))

print("A gráf csúcspontjai a szélességi bejárás szerint (a 0. csúcstól indulva):")
graf.BreadthFirstTraversal("0")
print("\nA gráf csúcspontjai a rekurzív szélességi bejárás szerint (a 0. csúcstól indulva):")
graf.rec_BreadthFirst("0")
