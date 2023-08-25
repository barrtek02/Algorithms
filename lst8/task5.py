from time import perf_counter

from matplotlib import pyplot as plt

from task4 import RobotsFleet4

def measure_time_of_function(function, a, b):

    start_time = perf_counter()

    if func.__name__ == fleet.linear_find.__name__:
        result = function(b)
    else:
        result = function(a, b)
    end_time = perf_counter()
    return round(end_time - start_time, 6)


fleet = RobotsFleet4()
times = [[] for i in range(5)]
n = range(2, 1000)
for i in n:
    fleet = RobotsFleet4()
    fleet.fill_robots(i)
    fleet.sort_robots('PRICE')


    for j, func in enumerate([fleet.linear_find, fleet.binary_find, fleet.hash_find]):
        if func.__name__ == fleet.hash_find.__name__:
            for y, alpha in enumerate([0.3, 0.5, 0.8]):
                size = int(len(fleet.robots) / alpha)
                fleet.hash_table = [None] * size
                for robot in fleet.robots:
                    fleet.hash_insert(robot, 'PRICE', alpha)
                times[j + y].append(measure_time_of_function(func, 'PRICE', [i]))

        else:
            times[j].append(measure_time_of_function(func, 'PRICE', [i]))






fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

axs[0].scatter(n, times[0], label='Linear')
axs[0].scatter(n, times[1], label='Binary', c='tab:purple')
axs[0].scatter(n, times[2], label='Hash - 0.3', c='tab:orange')
axs[0].legend()
plt.xlabel("n")

axs[1].scatter(n, times[1], label='Binary', c='tab:purple')
axs[1].scatter(n, times[2], label='Hash - 0.3', c='tab:orange')
axs[1].legend()
plt.xlabel("n")


axs[2].scatter(n, times[4], label='Hash - 0.8', c='tab:green', s=10)
axs[2].scatter(n, times[3], label='Hash - 0.5', c='tab:red', s=10)
axs[2].scatter(n, times[2], label='Hash - 0.3', c='tab:orange', s=10)
axs[2].legend()
plt.xlabel("n")


plt.tight_layout()
plt.show()