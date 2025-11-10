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
print("Kezdetben a gráf csúcsai: ",graf.getVertices())
print("Kezdetben a gráf élei: ",graf.getEdges(False))

print("\nFelvesszük a gráfba a (0,4) élt. Ez 2 létező csúcs összekötése.")
graf.addEdge("0","4",False)
print("A gráf élei most: ",graf.getEdges(False))

print("\nFelvesszük a gráfba a (10,5) élt. A 10-es eddig nem volt csúcs.")
graf.addEdge("10","5",False)
print("A gráf csúcsai most: ",graf.getVertices())
print("A gráf élei most: ",graf.getEdges(False))

print("\nFelvesszük a gráfba a (6,8) élt. A 8-as eddig nem volt csúcs.")
graf.addEdge("6","8",False)
print("A gráf csúcsai most: ",graf.getVertices())
print("A gráf élei most: ",graf.getEdges(False))

print("\nFelvesszük a gráfba a (12,13) élt. Egyik se volt még csúcs. Ezután a gráf nem összefüggő!")
graf.addEdge("12","13",False)
print("A gráf csúcsai most: ",graf.getVertices())
print("A gráf élei most: ",graf.getEdges(False))
