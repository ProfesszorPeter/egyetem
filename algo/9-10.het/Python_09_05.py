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

    def DepthFirstTraversal(self,start):   # MélységiBejárás; nem rekurzív megvalósítás;
        node=start                         # egy összefüggő gráfot tud csak bejárni;
        edge=0                                         
        node_stack = [node]  # a kezdőpontot betesszük egy üres verembe (Python-lista veremként)
        edge_stack=[edge]    # a 0 élsorszámot is betesszük egy másik verembe
        visited = set()  # üreshalmaz létrehozása
                         # A halmaz itt is arra szolgál, hogy ne dolgozzunk fel egy pontot
                         # többször.
                         # A veremre azért van szükség, hogy az egyes bejárt utakról vissza
                         # tudjunk térni az egyes elágazási pontokhoz, de az is kell, hogy
                         # melyik volt az utolsó él, amely mentén továbbhaladtunk, ezért
                         # az élt is vermelni kell. Az egyszerűség kedvéért két külön verem van
                         # (az egyik a pontoknak, a másik a hozzájuk tartozó éleknek).
                         # Amíg nem üres a verem, addig még van bejáratlan pont.
        while node_stack:              # amíg nem üres a pontverem, addig:
            if node not in visited:    # ha a pont nincs benne a halmazban:
                visited.add(node)      # akkor betesszük a halmazba, és
                print(node, end=' ')   # feldolgozzuk (azaz most kiírjuk);
            while (edge<=(len(self.Neighbors(node))-1) and  # az aktuális pont olyan szomszédját
                  (self.Neighbors(node)[edge] in visited)): # keressük, amelyik nincs benne a
                edge+=1                    # halmazban: ehhez az él sorszámát növelgetjük 1-gyel
            if (edge<=(len(self.Neighbors(node))-1)): # ha van ilyen szomszéd,
                node_stack.append(node)         # akkor a pontot és az él sorszámát 
                edge_stack.append(edge)         # (amelyen "továbbmegyünk") verembe tesszük,
                node=self.Neighbors(node)[edge] # majd az él másik végpontja (a talált szomszéd)
                edge=0                          # lesz az aktuális (bekerül a node-ba),
                                           # és a legelső (vagyis a 0.) szóba jöhető élt vesszük
            else:              # ha nem találtunk ilyen szomszédot (mind benne van a halmazban), 
                node=node_stack.pop() # akkor kivesszük a veremből a tetején lévő pontot és a
                edge=edge_stack.pop() # megfelelő élsorszámot,
                edge+=1               # majd növeljük az élsorszámot
                # (vagyis visszaléptünk egyet és próbáljuk másik "útvonalon" folytatni).

    def rec_DepthFirst(self,start,visited=None):  # MélységiBejárás; rekurzív megvalósítás
        if visited is None:                 # ha a visited halmaz nincs megadva:
            visited=set()                   # akkor legyen üres
        visited.add(start)                  # tegyük bele a halmazba a start pontot
        print(start,end=' ')                # írassuk ki a start pontot ("feldolgozás")
        for tmp in self.Neighbors(start):   # iteráljunk végig a start pont szomszédain tmp-vel
            if tmp not in visited:          # ha a tmp segédpont nincs a halmazban:
                self.rec_DepthFirst(tmp,visited) # rekurzív hívás átadva a tmp-t és a halmazt
        return                            # visszatérés


# főprogram - irányított gráf
os.system('cls')
szotar={
            
            
            
            
            
            
            
            
            
       }
ir_graf=Graph(szotar)
print("\nAz irányított gráf csúcsai:\n ",ir_graf.getVertices())
print("Az irányított gráf élei:\n ",ir_graf.getEdges())
if ir_graf.isEdge("6","2"):
    print("A gráfnak a (6,2) éle.")
else:
    print("A gráfnak a (6,2) nem éle.")
if ir_graf.isEdge("2","6"):
    print("A gráfnak a (2,6) éle.")
else:
    print("A gráfnak a (2,6) nem éle.")
print("Az 1-es csúcspont szomszédjai:")
print(ir_graf.Neighbors("1"))
print("Az irányított gráf csúcspontjai a szélességi bejárás szerint (a 0. csúcstól indulva):")
ir_graf.BreadthFirstTraversal("0")
print("\nAz irányított gráf csúcspontjai a rekurzív szélességi bejárás szerint (a 0. csúcstól indulva):")
ir_graf.rec_BreadthFirst("0")
print("\nAz irányított gráf csúcspontjai a mélységi bejárás szerint (a 0. csúcstól indulva):")
ir_graf.DepthFirstTraversal("0")
print("\nAz irányított gráf csúcspontjai a rekurzív mélységi bejárás szerint (a 0. csúcstól indulva):")
ir_graf.rec_DepthFirst("0") 