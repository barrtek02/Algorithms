import random
from time import perf_counter
import matplotlib.pyplot as plt

from task1 import prime_factors

def rgcd(a, b): #compare factors and multiply the same ones
    """GCD using prime factors"""

    a_factors = prime_factors(a)
    b_factors = prime_factors(b)

    common_factors = []
    i = 0
    j = 0
    while i < len(a_factors) and j < len(b_factors):
        if a_factors[i] == b_factors[j]:
            common_factors.append(a_factors[i])
            i += 1
            j += 1
        elif a_factors[i] < b_factors[j]:
            i += 1
        else:
            j += 1

    gcd = 1
    for factor in common_factors:
        gcd *= factor

    return gcd


def egcd(a, b):
    """GCD using Euclides algorithm"""

    if b==0:
        return a
    else:
        return egcd(b, a % b)

def test_cases():
    assert rgcd(12, 3) == 3
    assert rgcd(12, 20) == 4
    assert rgcd(34, 88) == 2
    assert egcd(12, 3) == 3
    assert egcd(12, 20) == 4
    assert egcd(34, 88) == 2
    assert rgcd(12, 18) == 6
    assert rgcd(24, 36) == 12
    assert rgcd(7, 11) == 1
    assert egcd(12, 18) == 6
    assert egcd(24, 36) == 12
    assert egcd(7, 11) == 1






def measure_time_of_function(function, a, b):

    start_time = perf_counter()
    result = function(a, b)
    end_time = perf_counter()
    return round(end_time - start_time, 6)

def test_performance(n, m):
    rgcd_times = []
    egcd_times = []
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    # format the RGB values as a string
    color = "#{:02x}{:02x}{:02x}".format(r, g, b)
    for q in range(1, m):

        rgcd_times.append(measure_time_of_function(rgcd, n, q))
        egcd_times.append(measure_time_of_function(egcd, n, q))
    plt.scatter(range(1, m), rgcd_times, c='red')
    plt.scatter(range(1, m), egcd_times, c='blue')
    plt.xlabel('q')
    plt.ylabel('Time')


if __name__ == '__main__':
    test_cases()
    n = [10, 50, 67, 97, 100, 111, 112, 150]
    n = [66]
    for n in n:
        test_performance(n, 100)
    plt.legend(['RGCD', 'EGCD'])
    plt.show()

