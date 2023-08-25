import random
import numpy as np


def random_graph(V, q):
    max_edges = V * (V - 1) // 2
    num_edges = int(q * max_edges)

    adjacency_matrix = np.zeros((V, V), dtype=int)
    incidence_matrix = np.zeros((V, num_edges), dtype=int)

    edge_count = 0
    while edge_count < num_edges:
        v1 = np.random.randint(0, V)
        v2 = np.random.randint(0, V)

        if v1 != v2 and adjacency_matrix[v1][v2] == 0:
            adjacency_matrix[v1][v2] = 1
            adjacency_matrix[v2][v1] = 1

            incidence_matrix[v1][edge_count] = 1
            incidence_matrix[v2][edge_count] = 1

            edge_count += 1

    return adjacency_matrix, incidence_matrix


if __name__ == '__main__':
    V, q = 5, 0.2
    adjacency_matrix, incidence_matrix = random_graph(V, q)

    print("Adjacency Matrix:")
    print(adjacency_matrix)
    print("Size:", adjacency_matrix.size)

    print('')

    print("Incidence Matrix:")
    print(incidence_matrix)
    print("Size:", incidence_matrix.size)
