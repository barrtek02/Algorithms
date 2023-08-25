from lst9.task2 import RobotsFleet6

class RobotsFleet7(RobotsFleet6):
    def __init__(self):
        super().__init__()

    def countSort(self, param, k, show=False):
        k += 1
        C = [0 for i in range(k)]
        B = [0 for i in range(len(self.robots))]

        for i in self.robots:
            C[i[param]] += 1

        if show:
            print(f'Index: {list(range(k))}')
            print(f'Count: {C}')

        for i in range(1, k):
            C[i] = C[i] + C[i - 1]
        if show:
            print(f'added Count: {C}')

        for i in self.robots[::-1]:
            if i[param] < k:
                if show:
                    print(B)
                B[C[i[param]] - 1] = i
                C[i[param]] -= 1

        self.robots = B

if __name__ == '__main__':


    fleet = RobotsFleet7()
    fleet.fill_robots(10)
    # fleet.fill_robots(99990)
    print('BEFORE countSort')
    fleet.display_fleet()
    param = 'PRICE'
    param = 'RANGE'
    max_param = max([i[param] for i in fleet.robots])
    fleet.countSort(param, max_param ,show=True)
    print('AFTER countSort')
    fleet.display_fleet()
