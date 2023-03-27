import networkx as nx
import matplotlib.pyplot as plt


Q = {'q0': {'a': 'q2', 'b': 'q2', 'c': 'q2'},
     'q1': {'a': 'q4', 'b': 'q0', 'c': 'q3'},
     'q2': {'a': 'q1', 'b': 'q1', 'c': 'q6'},
     'q3': {'a': 'q3', 'b': 'q3', 'c': 'q3'},
     'q4': {'a': 'q0', 'b': 'q5', 'c': 'q5'},
     'q5': {'a': 'q4', 'b': 'q4', 'c': 'q4'},
     'q6': {'a': 'q3', 'b': 'q3', 'c': 'q3'}}

start_input = 'q0'

def show_graph(state='q0', color='yellow' ):
    G = nx.DiGraph()
    G.add_nodes_from(list(Q.keys()))
    start_input = state
    node_colors = [color if node == start_input else 'white' for node in G.nodes()]

    Vx = {'q0': 0, 'q1': 1, 'q2': 2, 'q3': 3.5, 'q4': 1, 'q5': 2, 'q6': 3.5}
    Vy = {'q0': 1, 'q1': 1, 'q2': 1.5, 'q3': 1, 'q4': 0, 'q5': 0, 'q6': 2}
    pos = {}
    for v in G.nodes:
        pos[v] = [Vx[v], Vy[v]]

    G.add_edge('q0', 'q2', label='a, b, c', directed=True)
    G.add_edge('q1', 'q0', label='b', directed=True)
    G.add_edge('q1', 'q3', label='c',directed=True)
    G.add_edge('q1', 'q4', label='a', directed=True)
    G.add_edge('q2', 'q1', label='a, b', directed=True)
    G.add_edge('q2', 'q6', label='c', directed=True)
    G.add_edge('q3', 'q3', label='', directed=True)
    G.add_edge('q4', 'q0', label='a', directed=True)
    # G.add_edge('q4', 'q5', label='b, c', directed=True)
    G.add_edge('q5', 'q4', label='a, b, c', directed=True)
    G.add_edge('q6', 'q3', label='a, b, c', directed=True)

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_shape='o', edgecolors='black', node_size=500)
    nx.draw_networkx_edges(G, pos,connectionstyle='arc3, rad = 0.3', edgelist = [('q4','q5')])
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'label'), verticalalignment='bottom')
    nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle='->')
    nx.draw_networkx_labels(G, pos)
    Vx = {'q0': 0, 'q1': 1, 'q2': 2, 'q3': 3.5, 'q4': 1, 'q5': 2, 'q6': 3.5}
    Vy = {'q0': 1, 'q1': 1, 'q2': 1.5, 'q3': 1.3, 'q4': -0.1, 'q5': -0.1, 'q6': 2.2}
    pos = {}
    for v in G.nodes:
        pos[v] = [Vx[v], Vy[v]]
    nx.draw_networkx_edge_labels(G, pos, edge_labels={('q5', 'q4'): 'b, c'}, verticalalignment='top')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={('q3', 'q3'): 'a, b, c'}, label_pos=1)
    plt.axis('off')
    plt.tight_layout()
    plt.show()


# input_string = 'abca'
input_string = 'aba'

current_state = start_input
for symbol in input_string:
    show_graph(current_state)
    next_state = Q[current_state][symbol]
    print(f'{current_state} ------- {symbol} ------> {next_state}')
    current_state = next_state
print(f'Final state: {next_state}')
if current_state in ['q0', 'q4', 'q5']:
    print(f'Input string accepted')
    show_graph(current_state, 'green')
else:
    print(f'Input string not accepted')
    show_graph(current_state, 'red')

plt.show()