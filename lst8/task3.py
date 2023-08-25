from lst8.task2 import RobotsFleet2

class RobotsFleet3(RobotsFleet2):
    def __init__(self):
        super().__init__()
    def sort_robots(self, param):
        self.robots = sorted(self.robots, key=lambda x: x[param])
    def binary_find(self, param, values):
        def binary_find_idx(a):
            start, end = 0, len(self.robots)
            while True:
                if start >= end:
                    return None
                id = (start + end) // 2
                if self.robots[id][param] == a:
                    return id
                if a <= self.robots[id][param]:
                    end = id - 1
                else:
                    start = id + 1

        for value in values:
            idx = binary_find_idx(value)
            if idx is not None:
                return self.robots[idx]
        return f'No robot with "{param}" in {values}'




if __name__ == '__main__':
    fleet = RobotsFleet3()
    fleet.load_json('Robots1.json')
    fleet.display_fleet()
    fleet.sort_robots('TYPE')
    print(fleet.binary_find('TYPE', ['ASV', 'AGV']))
    fleet.sort_robots('PRICE')
    print(fleet.binary_find('PRICE', [100, 200, 300, 4163]))
    # fleet = RobotsFleet3()
    # fleet.fill_robots(100)
    # fleet.sort_robots('PRICE')
    # fleet.display_fleet()
    # print(len(fleet.robots))
    # print(fleet.binary_find('PRICE', [99]))

