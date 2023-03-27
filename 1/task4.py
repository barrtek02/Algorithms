import matplotlib.pyplot as plt
import networkx as nx
import random


n = 7
G = nx.Graph()

low, high = 0, 1
pos = {}
for i in range(n):
    x = random.uniform(low, high)
    y = random.uniform(low, high)
    pos[i] = (x, y)

G.add_nodes_from(range(n))
for i in G.nodes():
    for j in G.nodes():
        if i < j:
            R = random.random()
            if R < 0.3:
                G.add_edge(i, j)

nx.draw(G, pos, node_size=1000)
nx.draw_networkx_edges(G, pos)

plt.show()
