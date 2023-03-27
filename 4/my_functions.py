def max_element(list):
    max = list[0]
    for number in list:
        if number>max:
            max = number

    return max

def max2_element(list):
    max = list[0]
    max2 = list[1]

    for number in list:
        if number > max:
            max2 = max
            max = number
        elif number > max2:
            max2 = number

    return max, max2

def average(list):
    sum = 0
    for number in list:
        sum += number

    avg = sum/len(list)

    return avg

def matrix_multiplication(array1, array2):
    n = len(array1)
    new_array = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_array[i][j] += array1[i][k] * array2[k][j]
    return new_array

def subset_sum0(numbers):
    subset_sum0_value = False
    n = len(numbers)
    for i in range(1, 2**n):
        subset_sum = sum(numbers[j] for j in range(n) if (i & (1 << j)) != 0)
        if subset_sum == 0:
            subset_sum0_value = True
            break

    return subset_sum0_value