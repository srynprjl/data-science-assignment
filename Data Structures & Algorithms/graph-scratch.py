class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_nodes(self, node):
        if node not in self.graph:
            self.graph[node] = []
            print(f"Added node {node}")

    def add_edge(self, edge1, edge2):
        self.add_nodes(edge1)
        self.add_nodes(edge2)
        self.graph[edge1].append(edge2)
        print(f"Connected node {edge1} to {edge2}")

        if(not self.directed):
            self.graph[edge2].append(edge1)
            print(f"Connected node {edge2} to {edge1}")

    def get_neighbours(self, node):
        return self.graph.get(node, [])

    def display(self):
        for nodes, neighbours in self.graph.items():
            if(neighbours):
                print(f"{nodes} is directed to {neighbours}")
            else:
                print(f"{nodes} doesnt lead anywhere.")


graph = Graph(directed=True)
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_nodes('E')
graph.display()
print(f"Node A is connected to {graph.get_neighbours("A")}")


graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')
graph.add_nodes('E')
graph.display()
print(f"Node A is connected to {graph.get_neighbours("A")}")
