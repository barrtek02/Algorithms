import numpy as np
import random
from time import perf_counter
from recursive_alghoritms import *
import matplotlib.pyplot as plt



def generate_list(n):
    return [random.randint(1, 10000) for i in range(n)]


def measure_time_of_function(function, n):
    numbers = generate_list(n)

    start_time = perf_counter()
    result = function(numbers)
    end_time = perf_counter()
    return round(end_time - start_time, 6)

# zad1
n_user_input_1 = 10000
power_of_10 = 10
n_values_1 = [power_of_10]
while power_of_10 < n_user_input_1:
    power_of_10 *= 10
    n_values_1.append(power_of_10)
functions = [max_element_r, max2_element_r, average_r, merge_sort]
execution_times1 = [[] for function in functions]
for n in n_values_1:
    for i in range(len(functions)):
        execution_time = measure_time_of_function(functions[i], n)
        execution_times1[i].append(execution_time)

i = 0

plt.plot(n_values_1, (n_values_1*np.log(n_values_1))/10000000, label='nlogn')
id = {1:max_element_r.__name__,
      2:max2_element_r.__name__,
      3:average_r.__name__,
      4:merge_sort.__name__
      }
for times in execution_times1:
    i += 1
    plt.plot(n_values_1, times, label=f'{id[i]}')
plt.plot(n_values_1, np.array(n_values_1).flatten()/10000000, label='n')
plt.suptitle('O(nlogn)')
plt.legend()


plt.tight_layout()
plt.show()
