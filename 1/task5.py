import math
import random
from matplotlib.patches import Circle

import matplotlib.pyplot as plt
import networkx as nx

n = 100
G = nx.Graph()
pos = {}

low, high = 0, 1
r = 0.005
for i in range(n):
    count = 100
    while count > 0:
        count -= 1
        overlapping = False
        x = random.uniform(low, high)
        y = random.uniform(low, high)
        for center in pos.values():
            d = math.sqrt((center[0] - x) ** 2 + (center[1] - y) ** 2)
            if d < r * 2:
                overlapping = True
                break
        if not overlapping:
            pos[i] = (x, y)
            break


fig, ax = plt.subplots()
for pos_xy in pos.values():
    circle = Circle(pos_xy, r, fill=False)
    ax.add_patch(circle)

G.add_nodes_from(pos.keys())
for i in G.nodes():
    for j in G.nodes():
        if i < j:
            R = random.random()
            if R < 0.3:
                G.add_edge(i, j)

nx.draw(G, pos, node_size=1000)
nx.draw_networkx_labels(G, pos)
# nx.draw_networkx_edges(G, pos)

plt.show()
