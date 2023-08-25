from lst8.task3 import RobotsFleet3

class RobotsFleet4(RobotsFleet3):
    def __init__(self):
        super().__init__()
        self.hash_table = []



    def h(self, k, i):
        c = 1
        d = 5
        m = len(self.hash_table)
        # return k%4
        return (k%m + c*i + d*i*i)%m

    def hash_insert(self, x, key, alpha):
        i = 0
        m = len(self.hash_table)
        # sprawdzenie czy nowy element nie przekroczy współczynnika wypełnienia
        if len(self.robots)/len(self.hash_table) > alpha:
            return 'Full'
        while True:
            j = self.h(x[key], i)
            if self.hash_table[j] is None:
                self.hash_table[j]=x
                return j
            i+=1


    def hash_find(self, key, values):
        def hash_find_idx(k):
            i = 0
            m = len(self.hash_table)
            j = self.h(k, i)

            while True:
                j = self.h(k, i)

                # print(j)
                # print(self.hash_table)
                if self.hash_table[j] is None or i==m:
                    return None
                if self.hash_table[j][key]==k:
                    return j
                i+=1





        for value in values:
            idx = hash_find_idx(value)
            if idx is not None:
                return self.hash_table[idx]
        return 'None'





if __name__ == '__main__':
    fleet = RobotsFleet4()
    fleet.load_json('Robots1.json')
    alfa = 0.4
    size = int(len(fleet.robots) / alfa)
    fleet.hash_table = [None] * size

    fleet.display_fleet()
    fleet.sort_robots('PRICE')
    for robot in fleet.robots:
        fleet.hash_insert(robot, 'PRICE', alfa)

    print(fleet.hash_find('PRICE', [10000]))
    print(fleet.hash_find('PRICE', [8848]))

    # fleet = RobotsFleet4()
    # fleet.fill_robots(111)
    # size = int(len(fleet.robots) / 0.55)
    # fleet.hash_table = [None] * size
    # fleet.sort_robots('PRICE')
    # for robot in fleet.robots:
    #     fleet.hash_insert(robot, 'PRICE')
    # fleet.display_fleet()
    # # print(len(fleet.robots))
    # for i in range(111):
    #     print(fleet.hash_find('PRICE', [fleet.robots[i]['PRICE']]))

