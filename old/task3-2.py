import networkx as nx
import matplotlib.pyplot as plt

nodes = 6
graph = nx.Graph()
graph.add_nodes_from(range(1, nodes))
graph.add_edge(0, 1, weight=4)
graph.add_edge(0, 2, weight=4)
graph.add_edge(1, 2, weight=2)
graph.add_edge(1, 0, weight=4)
graph.add_edge(2, 0, weight=4)
graph.add_edge(2, 1, weight=2)
graph.add_edge(2, 3, weight=3)
graph.add_edge(2, 5, weight=2)
graph.add_edge(2, 4, weight=4)
graph.add_edge(3, 2, weight=3)
graph.add_edge(3, 4, weight=3)
graph.add_edge(4, 2, weight=4)
graph.add_edge(4, 3, weight=3)
graph.add_edge(5, 2, weight=2)
graph.add_edge(5, 4, weight=3)

def showGraph(graph):
    """Show graph with weights"""

    pos = nx.spring_layout(graph)
    nx.draw_networkx(graph, pos)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()


def kruskal(graph):
    """Create Minimum Spanning Tree by kruskal algorithm (returns new edges)"""

    def check_subset(subsets, i):
        """Define in which subset is given node"""

        if subsets[i] == i:
            return i
        return check_subset(subsets, subsets[i])


    def join_two_subsets(subsets, first, second):
        """Join two subsets into one"""
        first_root = check_subset(subsets, first)
        second_root = check_subset(subsets, second)

        subsets[first_root] = second_root

    #sort edges by weight (ascending)
    labels = nx.get_edge_attributes(graph, 'weight')
    edges = list(sorted(labels.items(), key=lambda item: item[1]))

    subsets = []
    result = []

    #create subsets with single elements
    for node in range(len(graph.nodes)):
        subsets.append(node)

    #there will be one n-1 edges in n node graph
    while len(result) < len(graph.nodes) - 1:

        #take the smallest edge, delete this edge for next iteration
        node1, node2 = edges[0][0]
        weight = edges[0][1]
        edges.pop(0)

        #check if node1 and node2 forms a cycle, if not add to result
        first_subset = check_subset(subsets, node1)
        second_subset = check_subset(subsets, node2)

        if first_subset != second_subset:
            result.append([node1, node2, weight])
            join_two_subsets(subsets, first_subset, second_subset)

    minimumCost = 0
    print("Edges in the Minimum Spanning Tree (Kruskal):")
    for node1, node2, weight in result:
        minimumCost += weight
        print(f"{node1} --- {node2} |  weight: {weight}")
    print("Minimum Spanning Tree cost: ", minimumCost)
    print('')
    return result


new_tree = kruskal(graph)
showGraph(graph)


def showGraphfromEdges(edges):
    """Show graph from edges"""

    minSpanTree = nx.Graph()
    minSpanTree.add_nodes_from(range(1, len(edges)))
    for edge in edges:
        minSpanTree.add_edge(edge[0], edge[1], weight=edge[2])
    pos = nx.spring_layout(minSpanTree)
    nx.draw_networkx(minSpanTree, pos)
    labels = nx.get_edge_attributes(minSpanTree, 'weight')
    nx.draw_networkx_edge_labels(minSpanTree, pos, edge_labels=labels)
    plt.show()

showGraphfromEdges(new_tree)

def prim(graph):
    """Create Minimum Spanning Tree by prim algorithm (returns new edges)"""

    graph_nodes = graph.nodes
    #convert graph to adjacency matrix
    graph = nx.to_pandas_adjacency(graph)

    visited = [0 for i in range(len(graph_nodes))]
    # choose first node
    visited[0] = True
    minimumCost = 0
    result = []
    print("Edges in the Minimum Spanning Tree (Prim):")
    #there will be nodes - 1 edges in result
    while len(result) < len(graph_nodes) - 1:

        minimum = float('inf')
        node1 = 0
        node2 = 0
        #iterate through every node in graph
        for i in range(len(graph_nodes)):
            if visited[i]:  #we must had visited node to go further to its neighbors
                for j in range(len(graph_nodes)):
                    if ((not visited[j]) and graph[i][j]): #if yet not visited, and there is an edge
                        if minimum > graph[i][j]: #choose minimum edge
                            minimum = graph[i][j]
                            node1 = i
                            node2 = j

        visited[node2] = True  #mark visited node, append result
        print(f"{node1} --- {node2} |  weight: {int(graph[node1][node2])}")
        minimumCost += int(graph[node1][node2])
        result.append([node1, node2, int(graph[node1][node2])])

    print("Minimum Spanning Tree cost: ", minimumCost)
    print('')
    return result

new_tree2 = prim(graph)
showGraphfromEdges(new_tree2)

