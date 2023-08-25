import random


class RobotLinkedList:
    def __init__(self):
        self.linkedlist = []
        self.head = None
        self.tail = None
        self.elems = 0

    def search(self, k, param):
        tmp = self.head
        while tmp is not None and self.linkedlist[tmp][1][param] !=k:
            tmp = self.linkedlist[tmp][2]

        if tmp is not None:
            return tmp
        else:
            return None

    def printLinkedList(self):
        current = self.linkedlist[self.head]  # Start from the head node

        # Traverse the linked list until the current node is None
        while current[2] is not None:
            print(current[1])  # Print the value of the current node
            current = self.linkedlist[current[2]]  # Move to the next node
        print(current[1])  # Print the value of the current node

    def insert(self, x):
        x=[None, x, None]
        if self.head is None:
            self.head = 0
            self.linkedlist.append(x)
            return

        next = self.head
        while self.linkedlist[next][2] is not None:
            next = self.linkedlist[next][2]

        self.linkedlist[next][2] = len(self.linkedlist)
        x[0] = next
        self.linkedlist.append(x)
        self.elems += 1

    def remove(self, x, param):
        if self.head is None:
            return

        x = self.search(x, param)
        if x is None:
            return f'No {x}'
        if self.linkedlist[x][0] is not None:
            self.linkedlist[self.linkedlist[x][0]][2] = self.linkedlist[x][2]
        else:
            self.head = self.linkedlist[self.linkedlist[x][2]]
        if self.linkedlist[x][2] is not None:
            self.linkedlist[self.linkedlist[x][2]][0] = self.linkedlist[x][0]
        self.linkedlist[x] = [None, None, None]
        self.elems -=1

    def sort(self, param):
        sorted_list = []
        for x in self.linkedlist:
            if x[1] is not None:
                sorted_list.append(x[1][param])
        sorted_list.sort()

        previous = None
        for j in range(len(sorted_list)):
            for i in range(len(self.linkedlist)):
                if self.linkedlist[i][1] is None:
                    continue
                if self.linkedlist[i][1][param] == sorted_list[j]:
                    self.linkedlist[i][0] = previous
                    previous = i

        next = None
        for j in range(len(sorted_list))[::-1]:
            for i in range(len(self.linkedlist)):
                if self.linkedlist[i][1] is None:
                    continue
                self.head=next
                if self.linkedlist[i][1][param] == sorted_list[j]:
                    self.linkedlist[i][2] = next
                    next = i

    def bubbleSort(self):
        n = len(self.linkedlist)
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if self.linkedlist[j][1]['PRICE'] > self.linkedlist[j + 1][1]['PRICE']:
                    swapped = True
                    self.linkedlist[j], self.linkedlist[j + 1] = self.linkedlist[j + 1], self.linkedlist[j]

            if not swapped:
                return

        # result = []
        n = len(self.linkedlist)

        # for i in range(n):
        #     if i == 0:
        #         result.append([None, self.linkedlist[i][1], i + 1])
        #     elif i == n - 1:
        #         result.append([i, self.linkedlist[i][1],None])
        #     else:
        #         result.append([i, self.linkedlist[i][1], i + 1])

        for i in range(n):
            if i == 0:
                self.linkedlist[i] = [None, self.linkedlist[i][1], i + 1]
            elif i == n - 1:
                self.linkedlist[i] = [i, self.linkedlist[i][1],None]
            else:
                self.linkedlist[i] = [i - 1, self.linkedlist[i][1], i + 1]

        # self.linkedlist = result

linkedList = RobotLinkedList()

#
# linkedList.insert(5)
# linkedList.insert(4)
# linkedList.insert(3)
# linkedList.insert(2)
# linkedList.insert(1)
# print(linkedList.linkedlist)
# print(linkedList.search(3))
# # linkedList.remove(3)
# print(linkedList.linkedlist)
# # linkedList.insert(3)
# print(linkedList.linkedlist)
# # linkedList.bubbleSort()
# # linkedList.swapNodes(2, 5)
# linkedList.sort()
# print(linkedList.linkedlist)

N = 5

price = random.sample(range(N * 3), N)
for i in range(N):
    robot = {"TYPE": random.choice(["AGV", "AFV", "ASV", "AUV"]), "PRICE": price[i],
             "RANGE": random.randint(0, 100), "CAMERA": random.randint(0, 1)}
    linkedList.insert(robot)

print('Linkedlist')
for x in linkedList.linkedlist:
    print(x)
print('')
print('Before sort')
linkedList.printLinkedList()
print('')
print('After sort')
# linkedList.sort('PRICE')
linkedList.bubbleSort()

print('')
for x in linkedList.linkedlist:
    print(x)
print('')

# linkedList.printLinkedList()

