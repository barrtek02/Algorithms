def countingSort(arr, col, k):
    n = len(arr)
    output = [0] * n

    max_val = k

    count = [0] * (max_val + 1) #count array

    for row in arr: #count
        count[row[col]] += 1

    # added count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # output array
    for row in reversed(arr):
        val = row[col]
        output[count[val] - 1] = row
        count[val] -= 1

    return output


def radixSort(matrix, k):
    # number of columns
    num_columns = len(matrix[0])

    # radix sort for each column
    for col in reversed(range(num_columns)):
        matrix = countingSort(matrix, col, k)

    return matrix


matrix = [
    [4, 2, 7],
    [1, 5, 2],
    [3, 5, 1],
    [4, 2, 3],
    [1, 5, 4]
]

sorted_matrix = radixSort(matrix, 12)

for row in matrix:
    print(row)
print('')
for row in sorted_matrix:
    print(row)
