import networkx as nx
import matplotlib.pyplot as plt
from random import random, randint, choice


graph = nx.Graph()

def random_Edges(graph, N_nodes, P):
    """Connect N_nodes with P propability"""

    graph.add_nodes_from(range(1, N_nodes + 1))
    for i in graph.nodes():
        for j in graph.nodes():
            if (i < j):
                R = random()
                if (R < P):
                    graph.add_edge(i, j, weight=randint(1, 5))

random_Edges(graph, 10, 0.5)

def showGraph(graph):
    """Show graph with weights"""

    pos = nx.spring_layout(graph)
    nx.draw_networkx(graph, pos)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

showGraph(graph)


def dijkstra(graph, start, end):
    """Dijkstra alghoritm printing shortest path from start to end"""

    visited = set()
    unvisited = set(graph.nodes)
    distances = {start: 0}
    shortest_paths = {start: [start]}
    #set distance inf to all nodes
    for node in unvisited:
        if node == start:
            continue
        else:
            distances[node] = float("inf")
    cur_node = start
    while len(unvisited) > 0:
        if cur_node == end:
            break
        #if all nodes have inf -> no path
        if min([distances[node] for node in unvisited]) == float("inf"):
            print('There is no path between u and v.')
            break
        connections = graph[cur_node]
        for node in connections:
            # if distance through current node is shorter then replace it
            if distances[cur_node] + graph[cur_node][node]["weight"] < distances[node]:
                distances[node] = distances[cur_node] + graph[cur_node][node]["weight"]
                shortest_paths[node] = shortest_paths[cur_node] + [node]
        # mark current_node as visited
        visited.add(cur_node)
        unvisited.remove(cur_node)
        # choose node with the minimum distance
        cur_node = sorted([(node, distances[node]) for node in unvisited], key=lambda x: x[1])[0][0]

    print(f"Path: {shortest_paths[end]}, Cost: {distances[end]}")
    weights = []
    for i in range(0, len(shortest_paths[end]) - 1):
        weights.append(graph[shortest_paths[end][i]][shortest_paths[end][i + 1]]["weight"])
    print(f"Weights between: {weights} ")

start = choice(list(graph.nodes))
end = choice(list(graph.nodes))
while end == start:
    end = choice(list(graph.nodes))
dijkstra(graph, start, end)
plt.show()
