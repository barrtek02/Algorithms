from lst12.task1 import Graph


class Graph2(Graph):
    def __init__(self):
        super().__init__()

    def topological_sort(self):
        Q = []
        color = {v: 'WHITE' for v in self.V}
        p = {v: None for v in self.V}
        t = 0
        G, pos, color = self.initialize_graph()
        self.draw_graph(color, G, pos)

        def dfs_visit(u, t):
            color[u] = 'GRAY'
            t += 1
            for v in self.E[u]:
                if color[v] == 'WHITE':
                    p[v] = u
                    dfs_visit(v, t)
            color[u] = 'BLACK'
            self.draw_graph(color, G, pos)

            t += 1

            Q.append(u)

        def dfs_full():
            for v in self.V:
                if color[v] == 'WHITE':
                    dfs_visit(v, t)


        dfs_full()

        if len(Q) == len(self.V):
            return Q
        else:
            return None


graph = Graph2()
graph.load_from_json('graph2.json')
sorted_order = graph.topological_sort()

if sorted_order is not None:
    print("Topological Sort Order:", sorted_order)
else:
    print("Graph contains cycle!")
