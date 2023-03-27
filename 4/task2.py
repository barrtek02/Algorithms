array1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

array2 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

def array_multiplication(array1, array2):
    n = len(array1)
    new_array = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_array[i][j] += array1[i][k] * array2[k][j]

    for row in new_array:
        print(row)

array_multiplication(array1, array2) #O(n^3)

