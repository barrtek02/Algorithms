import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=4)
G.add_edge('A', 'D', weight=4)
G.add_edge('A', 'E', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('C', 'B', weight=4)
G.add_edge('D', 'E', weight=3)

G = nx.Graph()
VV = ['A', 'B', 'C', 'D', 'E']
WW = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (3, 5)]
Vx = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}
Vy = {'A': 0, 'B': 1, 'C': 0, 'D': -1, 'E': 0}
g = nx.Graph()
gpos = {}
for v in VV:
    g.add_node(v)
    gpos[v] = [Vx[v], Vy[v]]

nx.draw(g, gpos)
nx.draw_networkx_edge_labels(g, gpos)
nx.draw_networkx_labels(G, gpos)
labels = nx.get_edge_attributes(g, 'weight')
nx.draw_networkx_edge_labels(g, gpos, edge_labels=labels)
plt.show()

plt.show()

