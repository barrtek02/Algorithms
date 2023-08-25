import random
import json

class RobotsFleet:
    def __init__(self):
        self.robots = []
        self.robot_types = ["AGV", "AFV", "ASV", "AUV"]


    def fill_robots(self, N):
        price = random.sample(range(N*3), N)
        for i in range(N):
            robot = {"TYPE": random.choice(self.robot_types), "PRICE": price[i],
                     "RANGE": random.randint(0, 100), "CAMERA": random.randint(0, 1)}
            self.robots.append(robot)

    def display_fleet(self):
        print(f"{'ID':<3}   {'TYPE':<5}  {'PRICE':<6} {'RANGE':<5} {'CAMERA':<5}")
        for i, robot in enumerate(self.robots):
            print(
                f"{str(i) + '.':>{len(str(len(self.robots)))+1}}    {robot['TYPE']:<5} {robot['PRICE']:<6} {robot['RANGE']:<5} {robot['CAMERA']:<10}")
        print('')
    def save_json(self, file_path):
        with open(file_path, "w") as f:
            json.dump(self.robots, f, indent=4)

    def load_json(self, file_path):
        with open(file_path, "r") as f:
            self.robots = json.load(f)

if __name__ == '__main__':
    fleet = RobotsFleet()
    fleet.fill_robots(10)
    # fleet.fill_robots(99990)
    fleet.display_fleet()
    # fleet.save_json('Robots1.json')
    # fleet.load_0json('Robots1.json')
    # fleet.save_json('Robots_times10.json')
