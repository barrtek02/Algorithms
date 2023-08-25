import random
from matplotlib import pyplot as plt
from lst9.task1 import RobotsFleet4

class RobotsFleet5(RobotsFleet4):
    def __init__(self):
        super().__init__()

    def heapSort(self, param, showHeap=False):
        def parent(i):
            return i // 2

        def left(i):
            return 2 * i + 1

        def right(i):
            return 2 * i + 2

        def heapify(A, hs, i):
            """A - list to sort
               hs - heap size
               i - root of subtree"""

            head = i
            l = left(i)
            r = right(i)

            if l < hs and A[l][param] > A[i][param]:
                head = l

            if r < hs and A[r][param] > A[head][param]:
                head = r

            if head != i:
                A[i], A[head] = A[head], A[i]
                ax.clear()
                plt.bar(range(len(A)), [robot[param] for robot in A], align='center')
                plt.pause(0.5)
                heapify(A, hs, head)

        def heapBuild(A):
            hs = len(A)
            for i in range(hs // 2 - 1, -1, -1):
                heapify(A, hs, i)

        fig, ax = plt.subplots()
        plt.bar(range(len(self.robots)), [robot[param] for robot in self.robots], align='center')
        plt.pause(0.5)
        heapBuild(self.robots)
        for i in range(len(self.robots) - 1, 0, -1):
            self.robots[i], self.robots[0] = self.robots[0], self.robots[i]
            ax.clear()
            plt.bar(range(len(self.robots)), [robot[param] for robot in self.robots], align='center')
            plt.pause(0.5)
            heapify(self.robots, i, 0)


class RobotsFleet6(RobotsFleet5):
    def __init__(self):
        super().__init__()

    def quickSort(self, param, l=0, u=None, ax=None):
        def partition(A, l, u, ax=None):
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
                    ax.clear()
                    plt.bar(range(len(A)), [robot[param] for robot in A], align='center')
                    plt.pause(0.5)
            if i<u:
                A[i + 1], A[u] = A[u], A[i + 1]
                ax.clear()
                ax.bar(range(len(A)), [robot[param] for robot in self.robots], align='center')
                plt.pause(0.5)
                return i + 1
            else:
                return i

        if u is None:
            u = len(self.robots) - 1

        if l < u:
            part = partition(self.robots, l, u, ax)
            self.quickSort(param, l, part - 1, ax)
            self.quickSort(param, part + 1, u, ax)


if __name__ == '__main__':
    fleet = RobotsFleet6()
    fleet.fill_robots(10)

    fleet2 = RobotsFleet6()
    fleet2.fill_robots(10)

    param = 'PRICE'


    fleet.heapSort(param, False)

    # Sortowanie szybkie
    fig, ax = plt.subplots()
    A = [robot[param] for robot in fleet2.robots]
    ax.bar(range(len(A)), A, align='center')
    plt.pause(0.5)

    fleet2.quickSort(param, ax=ax)


    plt.show()
