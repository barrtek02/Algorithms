from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import json


class Graph:
    def __init__(self, V=None):
        self.V = V
        self.E = defaultdict(list)

    def addEdge(self, u, v):
        self.E[u].append(v)

    def draw_graph(self, color, G, pos):
        node_colors = [color[node] for node in G.nodes()]
        nx.draw(G, pos, with_labels=True, node_color=node_colors,  font_color='blue', arrows=True)
        plt.show()

    def initialize_graph(self):
        G = nx.DiGraph()
        color = {v: 'WHITE' for v in self.V}  # Initialize color dictionary
        for u, v in self.E.items():
            G.add_edges_from([(u, v_i) for v_i in v])
        pos = nx.circular_layout(G)
        return G, pos, color

    def dfs(self):
        p = {}
        t = {}
        f = {}
        for node in self.V:
            p[node] = None
        time = 0

        G, pos, color = self.initialize_graph()
        self.draw_graph(color, G, pos)

        for node in self.V:
            if color[node] == 'WHITE':
                self.dfs_visit(node, color, time, t, f, p, G, pos)

    def dfs_visit(self, node, color, time, t, f, p, G, pos):
        color[node] = 'GREY'

        self.draw_graph(color, G, pos)

        time += 1
        t[node] = time
        for v in self.E[node]:
            if color[v] == 'WHITE':
                p[v] = node
                self.dfs_visit(v, color, time, t, f, p, G, pos)
        color[node] = 'BLACK'
        f[node] = f'{time}/{time+1}'

        self.draw_graph(color, G, pos)

    def bfs(self):
        s = '0'
        d = {v: float('inf') for v in self.V}
        p = {v: None for v in self.V}

        G, pos, color = self.initialize_graph()
        self.draw_graph(color, G, pos)

        color[s] = 'GREY'
        d[s] = 0
        p[s] = None

        Q = [s]
        while Q:
            u = Q.pop(0)
            for v in self.E[u]:
                if color[v] == 'WHITE':
                    color[v] = 'GREY'
                    d[v] = d[u] + 1
                    p[v] = u
                    Q.append(v)
                    # self.draw_graph(color, G, pos)

            color[u] = 'BLACK'

            self.draw_graph(color, G, pos)

    def save_to_json(self, file_path):
        data = {
            'V': self.V,
            'E': dict(self.E)
        }
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def load_from_json(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        self.V = data['V']
        self.E = defaultdict(list, data['E'])

if __name__ == '__main__':
    # V = ('u', 'v', 'w', 'x', 'y', 'z')
    # E = (('u', 'v'), ('u', 'x'), ('v', 'y'), ('x', 'v'), ('y', 'x'), ('w', 'y'), ('w', 'z'), ('z', 'z'))
    #
    # V = ('0', '1', '2', '3', '4', '5','6','7', '8', '9', '10')
    # E = (('0', '8'), ('0', '1'), ('1', '7'), ('1', '2'), ('2', '3'), ('3', '6'), ('6', '1'), ('3', '4'), ('4', '9'), ('4', '5'), ('5', '3'), ('5', '10'))
    #

    # for edge in E:
    #     graph.addEdge(edge[0], edge[1])

    # Call the dfs function
    # graph.save_to_json('koloskruskal.json')

    graph = Graph()
    graph.load_from_json('kolosdfs.json')
    graph.bfs()


    # Save the graph to JSON

    # Load the graph from JSON
    # loaded_graph = Graph()
    # loaded_graph.load_from_json('graph.json')

    # Call the dfs function on the loaded graph
    # loaded_graph.dfs()
