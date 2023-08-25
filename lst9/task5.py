import random

from lst9.task3 import RobotsFleet7
from lst9.task4 import radixSort
from time import perf_counter
from matplotlib import pyplot as plt

def measure_time_of_function(function, a, b):

    start_time = perf_counter()

    if function.__name__ == fleet.countSort.__name__ or function.__name__ == radixSort.__name__:
        result = function(a, b)
    else:
        result = function(a)
    end_time = perf_counter()
    return round(end_time - start_time, 6)


fleet = RobotsFleet7()
times = [[] for i in range(4)]
n = range(2, 1000, 100)
for i in n:

    for j, func in enumerate([fleet.heapSort, fleet.quickSort, fleet.countSort]):
        fleet = RobotsFleet7()
        fleet.fill_robots(i)
        times[j].append(measure_time_of_function(func, 'PRICE', i*3))

    inner =  outer = i
    random_lists = [[random.randint(0, 9) for _ in range(inner)] for _ in range(outer)]
    times[3].append(measure_time_of_function(radixSort, random_lists, i*4))

fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(16, 4))

axs[0].scatter(n, times[0], label='heapSort O(n)/O(nlogn)', c='tab:purple')
axs[0].legend()
plt.xlabel("n")

axs[1].scatter(n, times[1], label='quickSort O(n)/O(nlogn)', c='tab:orange')
axs[1].legend()
plt.xlabel("n")


axs[2].scatter(n, times[2], label='countSort O(n+k)', c='tab:green')
axs[2].legend()
plt.xlabel("n")

axs[3].scatter(n, times[3], label='radixSort w/countSort O(n+k)', c='tab:blue')
axs[3].legend()
plt.xlabel("n")


plt.tight_layout()
plt.show()