from random import randint
from time import perf_counter
import numpy as np
from matplotlib import pyplot as plt
from task1 import multiply_polynomials_naive
from task3 import multiply_poly_fft

def measure_time_of_function(function, a, b):

    start_time = perf_counter()
    result = function(a, b)
    end_time = perf_counter()
    return round(end_time - start_time, 6)

naive_times = []
fft_times = []

max_degree = 1000
degrees = range(max_degree, 1, -100)

numbers = 1, 11


for degree in degrees:
    poly1 = [randint(numbers[0], numbers[1]) for i in range(degree)]
    poly2 = [randint(numbers[0], numbers[1]) for i in range(degree)]

    naive_times.append(measure_time_of_function(multiply_polynomials_naive, poly1, poly2))
    fft_times.append(measure_time_of_function(multiply_poly_fft, poly1, poly2))

plt.scatter(degrees, naive_times, label="Naive")
plt.scatter(degrees, fft_times, label="FFT")
plt.xlabel("Degree")
plt.ylabel("Time (seconds)")
plt.legend()
plt.show()
