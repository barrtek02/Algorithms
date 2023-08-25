from lst10.task4 import random_graph


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1


def find_connected_components(adjacency_matrix):
    V = len(adjacency_matrix)
    ds = DisjointSet(V)

    for u in range(V):
        for v in range(u + 1, V):
            if adjacency_matrix[u][v] == 1:
                ds.union(u, v)

    components = {}
    for v in range(V):
        root = ds.find(v)
        if root in components:
            components[root].append(v)
        else:
            components[root] = [v]

    return list(components.values())



V, q = 100, 0.01


adjacency_matrix, _ = random_graph(V, q)

print("Adjacency Matrix:")
print(adjacency_matrix)

components = find_connected_components(adjacency_matrix)

print("Connected Components:")
for i, component in enumerate(components):
    print(i, component)
