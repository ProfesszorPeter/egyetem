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



        return weight

    def Neighbor(self, node):
        return self.dict.get(node)

    def dijkstra(self, source, target):
        not_visited = set(self.dict.keys())
        distance = {v: float('inf') for v in self.dict}
        distance[source] = 0
        previous = {}

        while not_visited:
            current = min((v for v in not_visited), key=lambda v: distance[v])
            if distance[current] == float('inf'):
                break
        

            not_visited.remove(current)
            for neighbor, w in self.dict.get(current, []):
                alt = distance[current] + w
                if alt < distance[neighbor]:
                    distance[neighbor] = alt
                    previous[neighbor] = current

        return distance, previous






inf = float("inf")

szotar = {
    "A": [("B", 6), ("C", 2), ("D", 4)],#0
    "B": [("E", 2), ("F", 5), ("D", 6)],#1
    "C": [("F", 1)],#2
    "D": [("H", 3)],#3
    "E": [],#4
    "F": [("I", 5)],#5
    "G": [("C", 7), ("H", 11)],#6
    "H": [],#7
    "I": [("G", 7)],#8
}


graf = Graf(szotar)
distance, previous = graf.dijkstra("A", "G")
print("Távolságok:", distance)
print("Előző csúcsok:", previous)
