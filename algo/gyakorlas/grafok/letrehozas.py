class Graph:
    def __init__(self, dict=None):
        if dict == None:
            dict = {}
        self.dict = dict
        
    def getCsucsok(self):
        return list(self.dict.keys())

    def getEl(self,iranyitott = True):
        elek = []
        for i in self.dict:
            print(f"i:{i}")
            for j in self.dict[i]:
                print(f"j:{j}")
                if iranyitott:
                    elek.append((i,j))
                elif (i,j) not in elek:
                    elek.append((i,j))
        return elek

    def addEL(self,x,y,iranyitott=True):
        self.dict[x].append(y)
        if not iranyitott:
            self.dict[y].append(x)
        print(f"sikerül hozzá adni az x:{x} y:{y} élt")

    def removeEl(self, x,y,iranyitott=True):
        self.dict[x].remove(y)
        if not iranyitott:
            self.dict[y].remove(x)
        print(f"sikerül törölni az x:{x} y:{y} élt")

    def Neighbors(self, x):
        return self.dict.get(x)

    def szelessegibejarasBFT(self,start):

        queue = [start]
        visited = set()
        visited.add(start)

        while queue:
            node = queue.pop(0)
            print(node)
            for tmp in self.Neighbors(node):
                if tmp not in visited:
                    queue.append(tmp)
                    visited.add(tmp)

    def melysegibejarasDFS(self,start):

        node = start
        edge = 0
        node_stack = [node]
        edge_stack = [edge]
        visited = set()

        while node_stack:
            if node not in visited:
                visited.add(node)
                print(node)
            while (edge <= (len(self.Neighbors(node))-1) and (self.Neighbors(node)[edge] in visited)):
                edge +=1
            if (edge <= (len(self.Neighbors(node))-1)):
                node_stack.append(node)
                edge_stack.append(edge)
                node = self.Neighbors(node)[edge]
                edge = 0
            else:
                node = node_stack.pop()
                edge = edge_stack.pop
                edge +=1




szotar = {
    "0": ["0", "2", "3"],
    "1": ["4", "5", "3"],
    "2": ["5"],
    "3": ["7"],
    "4": [],
    "5": ["8"],
    "6": ["2", "7"],
    "7": [],
    "8": ["6"],
}


graf = Graph(szotar)

print(graf.getCsucsok())
print(graf.getEl())
graf.addEL("4","3")
graf.removeEl("4","3")
graf.szelessegibejaras("2")
