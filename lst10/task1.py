import random


class RobotStack:
    def __init__(self, N):
        self.N = N
        self.stack = [None]*N
        self.top = -1

    def empty(self):
        return self.top == -1

    def full(self):
        return self.top  == self.N - 1

    def push(self, x):
        if self.full():
            return 'Full'
        else:
            self.top +=1
            self.stack[self.top] = x

    def pop(self):
        if self.empty():
            return 'Empty'
        else:
            self.top -= 1
            pop = self.stack[self.top + 1]
            self.stack[self.top + 1] = None
            return pop

    def clear(self):
        return [self.pop() for i in range(self.top + 1)]


stack = RobotStack(4)



N = 3

price = random.sample(range(N * 3), N)
for i in range(N):
    robot = {"TYPE": random.choice(["AGV", "AFV", "ASV", "AUV"]), "PRICE": price[i],
             "RANGE": random.randint(0, 100), "CAMERA": random.randint(0, 1)}
    stack.push(robot)

print(stack.stack)
print(stack.pop())
print(stack.clear())
print(stack.top)
print(stack.stack)