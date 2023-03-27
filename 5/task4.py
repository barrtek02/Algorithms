# Algorytm wyznaczania minimalnej ścieżki między dwoma zadanymi wierzchołkami w nieskierowanym grafie nieważonym metodą rekurencyjną można zaimplementować korzystając z algorytmu przeszukiwania grafu w głąb (DFS).
def find_shortest_path(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    if start == end:
        return 0
    min_path = float('inf')
    for neighbor in graph[start]:
        if neighbor not in visited:
            path = find_shortest_path(graph, neighbor, end, visited)
            if path < min_path:
                min_path = path
    return min_path + 1 if min_path != float('inf') else float('inf')


def find_shortest_path(graph, start, end, visited=None):
    if start not in graph:
        return float('inf')
    if visited is None:
        visited = set()
    visited.add(start)
    if start == end:
        return 0
    min_path = float('inf')
    for neighbor in graph[start]:
        if neighbor not in visited:
            path = find_shortest_path(graph, neighbor, end, visited)
            if path < min_path:
                min_path = path
    return min_path + 1 if min_path != float('inf') else float('inf')

def find_shortest_path(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    if start == end:
        return 0
    if start not in graph or end not in graph:
        return float('inf')
    min_path = float('inf')
    for neighbor in graph[start]:
        if neighbor not in visited:
            path = find_shortest_path(graph, neighbor, end, visited)
            if path < min_path:
                min_path = path
    return min_path + 1 if min_path != float('inf') else float('inf')

def test_find_shortest_path():
    # Test Case 1: Empty Graph
    graph1 = {}
    assert find_shortest_path(graph1, 'A', 'B') == float('inf')
    assert find_shortest_path(graph1, 'C', 'D') == float('inf')

    # Test Case 2: Graph with one node
    graph2 = {'A': []}
    assert find_shortest_path(graph2, 'A', 'A') == 0

    # Test Case 3: Graph with two nodes
    graph3 = {'A': ['B'], 'B': ['A']}
    assert find_shortest_path(graph3, 'A', 'B') == 1

    # Test Case 4: Graph with multiple nodes
    graph4 = {'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'], 'D': ['B'], 'E': ['B', 'F'], 'F': ['C', 'E']}
    assert find_shortest_path(graph4, 'A', 'F') == 3

    # Test Case 5: Unreachable node
    graph5 = {'A': ['B'], 'B': ['A'], 'C': []}
    assert find_shortest_path(graph5, 'A', 'C') == float('inf')

    graph1 = {'A': ['B', 'C'], 'B': ['C'], 'C': ['D'], 'D': ['E'], 'E': ['F']}
    assert find_shortest_path(graph1, 'A', 'F') == 4
    assert find_shortest_path(graph1, 'A', 'D') == 3
    assert find_shortest_path(graph1, 'B', 'F') == 4

    graph2 = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': ['H', 'I'], 'E': ['J', 'K'], 'F': ['L', 'M']}
    assert find_shortest_path(graph2, 'A', 'L') == 4
    assert find_shortest_path(graph2, 'A', 'J') == 3
    assert find_shortest_path(graph2, 'B', 'G') == 3

    graph3 = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': ['H', 'I'], 'E': ['J', 'K'], 'F': ['L', 'M'], 'N': []}
    assert find_shortest_path(graph3, 'A', 'N') == float('inf')

    graph4 = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': ['H', 'I'], 'E': ['J', 'K'], 'F': ['L', 'M']}
    assert find_shortest_path(graph4, 'A', 'F') == 3
    print("All test cases pass")

test_find_shortest_path()



# Algorytm ten działa następująco:
#
# Dodajemy wierzchołek startowy do zbioru odwiedzonych.
#
# Jeśli start i end są tym samym wierzchołkiem, to zwracamy 0, jako minimalną ścieżkę.
#
# W przeciwnym przypadku przechodzimy przez każdego sąsiada wierzchołka startowego i wywołujemy rekurencyjnie funkcję dla każdego sąsiada, z wyjątkiem już odwiedzonych wierzchołków.
#
# Dla każdego wyniku rekurencyjnego dodajemy 1, ponieważ przechodzimy z wierzchołka startowego do tego sąsiada. Następnie zwracamy minimalną wartość z wyników lub nieskończoność, jeśli nie istnieje ścieżka między start a end.
#
# Złożoność czasowa algorytmu to O(E + V), gdzie E to liczba krawędzi, a V to liczba wierzchołków w grafie. Algorytm przeszukuje graf w głąb i odwiedza każdy wierzchołek i krawędź dokładnie raz.
