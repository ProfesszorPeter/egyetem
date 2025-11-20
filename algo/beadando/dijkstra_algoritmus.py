class Graf:

    def __init__(self, dict=None):
        if dict == None:
            dict = {}
        self.dict = dict

    def getEdge(self, directed=True):
        edges = []
        for i in self.dict:
            for j in self.dict[i]:
                if directed:
                    edges.append((i, j))
                elif (i, j)not in edges:
                    edges.append((i, j))
        return edges

    def getVertices(self):
        return list(self.dict.keys())

    def Neighbor(self, node):
        return self.dict.get(node)

    def dijkstra(self, from_node, to_node):
        visited = set()
        feather = 100000000000
        print(f"honnan: {from_node}, hova {to_node}")
        for neighbors, weights in self.Neighbor(from_node):
            print(f"szomszéd: {neighbors}, súly: {weights}")
            if weights < feather:
                visited.add(neighbors)
        feather = weights
        print(feather)
        print(visited)



szotar = {
    "A": [("A", 6), ("C", 2), ("D", 4)],
    "B": [("E", 2), ("F", 5), ("D", 6)],
    "C": [("F", 1)],
    "D": [("H", 3)],
    "E": [],
    "F": [("I", 5)],
    "G": [("C", 7), ("H", 11)],
    "H": [],
    "I": [("G", 7)],
}


graf = Graf(szotar)
print(graf.Neighbor("A"))

graf.dijkstra("A", "D")
