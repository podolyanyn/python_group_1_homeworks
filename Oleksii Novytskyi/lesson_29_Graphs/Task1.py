class Graphs:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

    def getEdges(self):
        edges = []
        for i in self.gdict:
            for j in self.gdict[i]:
                if {i, j} not in edges:
                    edges.append({i, j})
        return edges

    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []

    def AddEdge(self, vrtx1, vrtx2):
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

    def get_transpose(self):
        g = Graphs(self.gdict)
        for v in self.gdict:
            for neighbor in self.gdict[v]:
                g.AddEdge(neighbor, v)
        return g


    # for print_scc useg
    def DFS(self, v, visited, stack):
        visited[v] = True
        for neighbor in self.gdict[v]:
            if neighbor not in visited or not visited[neighbor]:
                self.DFS(neighbor, visited, stack)
        stack.append(v)

    def print_scc(self):
        stack = []
        visited = {v: False for v in self.gdict}
        for v in self.gdict:
            if not visited[v]:
                self.DFS(v, visited, stack)
        transposed_graph = self.get_transpose()
        visited = {v: False for v in self.gdict}
        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                transposed_graph.DFS(v, visited, component)
                return component


graph = {
  '5': ['8', '2'],
  '3': ['2', '4'],
  '7': ['8'],
  '2': [],
  '4': ['8'],
  '8': []
}

g = Graphs(graph)
g.addVertex(5)
print(g.getVertices())
print(g.getEdges())
g.AddEdge(5,3)
g.AddEdge(3,7)
g.AddEdge(7,5)
print(g.getVertices())
print(g.print_scc())

