import math

import matplotlib.pyplot as plt
from my_functions import *
import random
from time import perf_counter

def generate_list(n):
    return [random.randint(1, 10000) for i in range(n)]

def generate_matrix(n):
    return [[random.randint(1, 10000) for i in range(n)] for j in range(n)]

def measure_time_of_function(function, n):

    if function.__name__ == 'matrix_multiplication':
        array1 = generate_matrix(n)
        array2 = generate_matrix(n)

        start_time = perf_counter()
        result = function(array1, array2)
        end_time = perf_counter()
    else:
        numbers = generate_list(n)

        start_time = perf_counter()
        result = function(numbers)
        end_time = perf_counter()

    return round(end_time - start_time, 6)

# zad1
n_user_input_1 = 100000
power_of_10 = 10
n_values_1 = [power_of_10]
while power_of_10 < n_user_input_1:
    power_of_10 *= 10
    n_values_1.append(power_of_10)

execution_times1 = [[], [], []]
functions = [max_element, max2_element, average]
for n in n_values_1:
    for i in range(len(functions)):
        execution_time = measure_time_of_function(functions[i], n)
        execution_times1[i].append(execution_time)

# zad2
n_user_input_2 = 150
n_values_2 = list(range(10, n_user_input_2+1, 10))
execution_times2 = []
for n in n_values_2:
    execution_time = measure_time_of_function(matrix_multiplication, n)
    execution_times2.append(execution_time)

# zad3
n_user_input_3 = 15
n_values_3 = list(range(1, n_user_input_3+1, 1))
execution_times3 = []
for n in n_values_3:
    execution_time = measure_time_of_function(subset_sum0, n)
    execution_times3.append(execution_time)



fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

i = 0
for times in execution_times1:
    i+=1
    axs[0].plot(n_values_1, times, label=f'zad1-{i}')
axs[0].set_title('O(n)')
axs[0].legend()
plt.xlabel("n")


axs[1].plot(n_values_2, execution_times2, 'tab:purple',  label='zad2')
axs[1].set_title('O(n^3)')
axs[1].legend()


axs[2].plot(n_values_3, execution_times3, 'tab:red', label='zad3')
axs[2].set_title('O(n*2^n)')
axs[2].legend()

fig.suptitle('Execution times')
for ax in axs.flat:
    ax.set(xlabel='n', ylabel='time')
plt.tight_layout()
plt.show()
