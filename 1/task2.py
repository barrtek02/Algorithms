import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
VV = ['A', 'B', 'C', 'D', 'E']
Vx = {'A': 1.5, 'B': 3, 'C': 3, 'D': 0, 'E': 0}
Vy = {'A': 1.5, 'B': 3, 'C': 0, 'D': 0, 'E': 3}

gpos = {}
for v in VV:
    G.add_node(v)
    gpos[v] = [Vx[v], Vy[v]]

G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('A', 'D')
G.add_edge('A', 'E', weight=4)
G.add_edge('B', 'C', weight=2)
G.add_edge('C', 'B', weight=4)
G.add_edge('D', 'E', weight=3)

nx.draw(G, gpos, with_labels=True ,node_size=1000)
nx.draw_networkx_edges(G, gpos)

plt.show()
