import networkx as nx
import matplotlib.pyplot as plt
from random import random


graph = nx.Graph()

def random_Edges(graph, N_nodes, P):
    graph.add_nodes_from(range(1, N_nodes + 1))
    for i in graph.nodes():
        for j in graph.nodes():
            if (i < j):
                R = random()
                if (R < P):
                    graph.add_edge(i, j)

random_Edges(graph, 10, 0.15)



def connected_components(graph):
    """Show connected components in graph"""
    visited = set()
    for node in graph:
        if node not in visited:
            connections = bfs(graph, node)
            visited.update(connections)
            yield connections


def bfs(graph, source):
    """BFS through graph from source"""
    visited = set()
    nearNodes = {source}
    while nearNodes:
        currentNodes = nearNodes #source
        nearNodes = set() #clear nearNodes
        for node in currentNodes:
            if node not in visited:
                visited.add(node)
                nearNodes.update(graph[node]) #add neighbors of node to nearNodes

    return visited


nx.draw_networkx(graph)
print(f"Graph Nodes: {graph.nodes}")
print(f"Connected components: {list(connected_components(graph))}")

plt.show()
