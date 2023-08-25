from lst9.task1 import RobotsFleet5

class RobotsFleet6(RobotsFleet5):
    def __init__(self):
        super().__init__()

    def quickSort(self, param, l=0, u=None, show=False):
        if u is None:
            u = len(self.robots) - 1

        def partition(A, l, u):
            """Lomuto
               A - list to sort
               l - lower bound
               u - upper bound"""

            x = A[u][param]
            i = l - 1
            for j in range(l, u):
                if A[j][param] <= x:
                    i += 1
                    A[i], A[j] = A[j], A[i]

            A[i + 1], A[u] = A[u], A[i + 1]   # Swap the pivot element with the greater element specified by i
            if show:
                print([robot[param] for robot in A], f'pivot: {A[i + 1][param]}')


            return i + 1

        if l < u:
            pivot = partition(self.robots, l, u)
            self.quickSort(param, l, pivot - 1, show)
            self.quickSort(param, pivot + 1, u, show)

if __name__ == '__main__':
    fleet = RobotsFleet6()
    fleet.fill_robots(10)
    # fleet.fill_robots(99990)
    print('BEFORE quickSort')
    fleet.display_fleet()
    fleet.quickSort('PRICE', show=True)
    print('AFTER quickSort')
    fleet.display_fleet()
    # fleet.save_json('Robots1.json')
    # fleet.load_json('Robots1.json')
    # fleet.save_json('Robots_times10.json')