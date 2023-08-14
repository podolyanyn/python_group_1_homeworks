class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = []

    def add_edge(self, source, destination):
        self.graph[source].append(destination)

    def get_vertices(self):
        return list(self.graph.keys())

    def get_edges(self):
        edges = []
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                edges.append((vertex, neighbor))
        return edges

    def dfs(self, vertex, visited, stack):
        visited[vertex] = True
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)
        stack.append(vertex)

    def get_transposed_graph(self):
        transposed_graph = Graph()
        for vertex in self.graph:
            transposed_graph.add_vertex(vertex)
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                transposed_graph.add_edge(neighbor, vertex)
        return transposed_graph

    def strongly_connected_components(self):
        visited = {vertex: False for vertex in self.graph}
        stack = []

        for vertex in self.graph:
            if not visited[vertex]:
                self.dfs(vertex, visited, stack)

        transposed_graph = self.get_transposed_graph()

        visited = {vertex: False for vertex in self.graph}
        components = []

        while stack:
            vertex = stack.pop()
            if not visited[vertex]:
                component = []
                transposed_graph.dfs(vertex, visited, component)
                components.append(component)

        return components



graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")

graph.add_edge("A", "B")
graph.add_edge("B", "C")
graph.add_edge("C", "D")

verticles = graph.get_vertices()
print(verticles)

edges = graph.get_edges()
print(edges)

print(graph.strongly_connected_components())