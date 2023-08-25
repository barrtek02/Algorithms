from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import json


class Graph3:
    def __init__(self, V=None):
        self.V = V
        self.E = defaultdict(list)

    def addEdge(self, u, v, weight):
        self.E[u].append((v, weight))
        self.E[v].append((u, weight))

    def initialize_graph(self):
        G = nx.Graph()
        color = {v: 'WHITE' for v in self.V}  # Initialize color dictionary
        for u, v_list in self.E.items():
            for v, weight in v_list:
                G.add_edge(u, v, weight=weight)
                G[u][v]['label'] = str(weight)  # Add edge label with weight
        pos = nx.spring_layout(G)
        return G, pos, color

    def draw_graph_simple(self, color, G, pos):
        node_colors = [color[node] for node in G.nodes()]
        nx.draw(G, pos, with_labels=True, node_color=node_colors,  font_color='blue', arrows=True)
        plt.show()

    def draw_graph(self, G, pos, edges, edge_colors):
        edge_labels = nx.get_edge_attributes(G, 'label')  # Get edge labels from 'label' attribute
        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=edge_colors)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # Use edge_labels directly
        plt.show()

    def MST(self, start_vertex):
        mst_edges = set()
        subsets = {}

        def make_set(v):
            subsets[v] = {'parent': v, 'rank': 0}

        def find_set(v):
            if subsets[v]['parent'] != v:
                subsets[v]['parent'] = find_set(subsets[v]['parent'])
            return subsets[v]['parent']

        def union(u, v):
            root_u = find_set(u)
            root_v = find_set(v)

            if subsets[root_u]['rank'] < subsets[root_v]['rank']:
                subsets[root_u]['parent'] = root_v
            elif subsets[root_u]['rank'] > subsets[root_v]['rank']:
                subsets[root_v]['parent'] = root_u
            else:
                subsets[root_v]['parent'] = root_u
                subsets[root_u]['rank'] += 1

        for v in self.V:
            make_set(v)

        sorted_edges = sorted([(u, v, w) for u, v_list in self.E.items() for v, w in v_list], key=lambda x: x[2])

        G, pos, color = self.initialize_graph()

        for u, v, weight in sorted_edges:
            if find_set(u) != find_set(v):
                mst_edges.add((u, v))
                union(u, v)

                G.add_edge(u, v, weight=weight)
                color[(u, v)] = 'blue'
                self.draw_graph(G, pos, mst_edges, list(color.values()))

        non_blue_edges = [(u, v) for (u, v) in G.edges() if color.get((u, v), '') != 'blue']
        G.remove_edges_from(non_blue_edges)
        self.draw_graph(G, pos, mst_edges, list(color.values()))

        return mst_edges

    def save_to_json(self, file_path):
        data = {
            'V': self.V,
            'E': {u: [[v, w] for v, w in v_list] for u, v_list in self.E.items()}
        }
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def load_from_json(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        self.V = data['V']
        self.E = defaultdict(list, {u: [[v, w] for v, w in v_list] for u, v_list in data['E'].items()})


if __name__ == '__main__':
    graph = Graph3(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    graph.addEdge("0", "1", 6)
    graph.addEdge("0", "8", 3)
    graph.addEdge("8", "7", 3)
    graph.addEdge("1", "7", 4)
    graph.addEdge("1", "6", 7)
    graph.addEdge("7", "6", 6)
    graph.addEdge("1", "2", 2)
    graph.addEdge("2", "3", 2)
    graph.addEdge("6", "3", 3)
    graph.addEdge("3", "4", 5)
    graph.addEdge("3", "5", 4)
    graph.addEdge("4", "9", 3)
    graph.addEdge("4", "5", 7)
    graph.addEdge("5", "10", 1)
    graph.save_to_json('koloskruskal.json')
    print(graph.MST("0"))

    # graph = Graph3()
    # graph.load_from_json('graph3.json')
    # G, pos, color = graph.initialize_graph()
    # graph.draw_graph_simple(color, G, pos)
    # print(graph.MST("a"))
