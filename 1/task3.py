import matplotlib.pyplot as plt
import networkx as nx

n = int(input("Please insert number of nodes: "))
G = nx.complete_graph(n)
pos = nx.circular_layout(G)
fig = plt.figure(figsize=(5, 5))

nx.draw_networkx_nodes(G, pos, node_size = 1000)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)

plt.show()
