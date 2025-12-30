import networkx
graph = networkx.Graph()

graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("C", "D")
graph.add_edge("C", "B")
graph.add_edge("D", "A")

nodes = ["A", "B", "C", "D", "E"]
for i in nodes:
    print(f"{i} :", end=" ")
    for j in graph.neighbors(i):
        print(j, end=" ")
    print()
