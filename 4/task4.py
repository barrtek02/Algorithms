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

    print(f"Execution time of {function.__name__}: {round(end_time - start_time, 6)} seconds")



# zad1 O(n)
n = 10000
measure_time_of_function(max_element, n)
measure_time_of_function(max2_element, n)
measure_time_of_function(average, n)
print()

# zad2 O(n^3)
n = 100
measure_time_of_function(matrix_multiplication, n)
print()
# zad3 O(2^n*n)
n = 17
measure_time_of_function(subset_sum0, n)