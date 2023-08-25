from matplotlib import pyplot as plt

from lst8.task4 import RobotsFleet4

class RobotsFleet5(RobotsFleet4):
    def __init__(self):
        super().__init__()

    def heapSort(self, param, show=False):

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
                heapify(A, hs, head)


        def heapBuild(A):
            hs = len(A)
            for i in range(hs // 2 - 1, -1, -1):
                heapify(A, hs, i)

        heapBuild(self.robots)
        for i in range(len(self.robots) - 1, 0, -1):

            self.robots[i], self.robots[0] = self.robots[0], self.robots[i]

            heapify(self.robots, i, 0)
            if show:
                heap = [i[param] for i in self.robots]
                print(heap)



if __name__ == '__main__':
    fleet = RobotsFleet5()
    fleet.fill_robots(10)
    # fleet.fill_robots(99990)
    print('BEFORE heapSort')
    fleet.display_fleet()
    fleet.heapSort('PRICE', show=True)
    print('AFTER heapSort')
    fleet.display_fleet()
    # fleet.save_json('Robots1.json')
    # fleet.load_json('Robots1.json')
    # fleet.save_json('Robots_times10.json')

