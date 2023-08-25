import json
from collections import defaultdict

import networkx as nx
from matplotlib import pyplot as plt

from lst12.task3 import Graph3


class Graph4(Graph3):
    def __init__(self):
        super().__init__()



    def dijkstra(self, start_vertex, end_vertex):
        # Dijkstra's algorithm implementation
        distances = {vertex: float('inf') for vertex in self.V}
        distances[start_vertex] = 0
        visited = set()
        G, pos, color = self.initialize_graph()

        shortest_path_edges = []
        self.draw_graph(shortest_path_edges, distances, G, pos)

        while len(visited) < len(self.V):
            current_vertex = min(set(distances.keys()) - visited, key=lambda x: distances[x])
            visited.add(current_vertex)

            if current_vertex == end_vertex:
                break

            for neighbor, weight in self.E[current_vertex]:
                new_distance = distances[current_vertex] + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

                    # Update shortest path edges
                    shortest_path_edges.append((current_vertex, neighbor))

                    # Draw the graph with updated distances and labels
            self.draw_graph(shortest_path_edges, distances, G, pos)

        return distances[end_vertex]

    def initialize_graph(self):
        G = nx.Graph()
        color = {v: 'WHITE' for v in self.V}  # Initialize color dictionary
        for u, v_list in self.E.items():
            for v, weight in v_list:
                G.add_edge(u, v, weight=weight)
                G[u][v]['label'] = str(weight)  # Add edge label with weight
        pos = nx.spring_layout(G)
        return G, pos, color
    def draw_graph(self, shortest_path_edges, distances, G, pos):

        nx.draw(G, pos, with_labels=False, node_color='lightblue', node_size=500)
        nx.draw_networkx_edges(G, pos, edgelist=shortest_path_edges, edge_color='red')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # Update node labels with distances and adjust positions
        node_labels = {node: f"{node} ({distances[node]})" for node in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10,
                                font_color='black', verticalalignment='center', horizontalalignment='center')

        plt.show()


graph = Graph4()
graph.load_from_json('graph3.json')
distances = graph.dijkstra("a", "f")
print(distances)
