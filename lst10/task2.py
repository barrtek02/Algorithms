import random


class RobotQueue:
    def __init__(self, N):
        self.N = N
        self.queue = [None] * N
        self.head = 0
        self.tail = 0

    def empty(self):
        return self.head == self.tail

    def full(self):
        tmp = self.tail + 1
        if tmp==self.N:
            tmp = 0
        return self.head == tmp

    def enqueue(self, x):
        if self.full():
            return 'Full'
        self.queue[self.tail] = x
        if self.tail + 1 == 0:
            self.tail = 0
        else:
            self.tail += 1

    def dequeue(self):
        if self.empty():
            return 'Empty'
        tmp = self.queue[self.head]
        self.queue[self.head] = None
        if self.head + 1 == self.N:
            self.head = 0
        else:
            self.head += 1
        return tmp

    def clear(self):
        return [self.dequeue() for i in range(self.head + 1)]


queue = RobotQueue(4)



N = 3

price = random.sample(range(N * 3), N)
for i in range(N):
    robot = {"TYPE": random.choice(["AGV", "AFV", "ASV", "AUV"]), "PRICE": price[i],
             "RANGE": random.randint(0, 100), "CAMERA": random.randint(0, 1)}
    queue.enqueue(robot)

print(queue.queue)
print(queue.head)
print(queue.tail)
print(queue.dequeue())
print(queue.clear())
print(queue.queue)
# print(queue.head)
# print(queue.tail)
