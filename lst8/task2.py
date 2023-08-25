from lst8.task1 import RobotsFleet

class RobotsFleet2(RobotsFleet):
    def __init__(self):
        super().__init__()
    def linear_find(self, params):
        for robot in self.robots:
            found = True
            for i, param in enumerate(params):
                if param is None:
                    continue
                elif isinstance(param, list):
                    if robot[list(robot.keys())[i]] not in param:
                        found = False
                        break
                elif robot[list(robot.keys())[i]] != param:
                    found = False
                    break
            if found:
                return f"Matching robot {robot}"

        return f"No matching robot to: {params}"


if __name__ == '__main__':
    fleet = RobotsFleet2()
    fleet.load_json('Robots1.json')
    fleet.display_fleet()
    print(fleet.linear_find(["AGV", None, [5, 6, 7, 8, 9, 10], 1]))
    print(fleet.linear_find(["AGV", 12, [5, 6, 7, 8, 9, 10], 1]))

