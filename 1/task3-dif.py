import matplotlib.pyplot as plt
import networkx as nx
import math

n = int(input("Please insert number of nodes: "))
G = nx.Graph()
G.add_nodes_from(range(n))
pos = {}
for i in range(n):
    angle = 2 * math.pi * i / n
    x = math.cos(angle)
    y = math.sin(angle)
    pos[i] = (x, y)

for i in range(n):
    for j in range(i + 1, n):
        G.add_edge(i, j)


fig = plt.figure(figsize=(5, 5))
nx.draw_networkx_nodes(G, pos, node_size = 1000)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)

plt.show()
