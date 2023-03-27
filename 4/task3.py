
numbers = [4, 2, 3, -4]
print(numbers)
print()
def subset_sum0(numbers):
    subset_sum0_value = False
    n = len(numbers)
    for i in range(1, 2**n):
        subset_sum = sum(numbers[j] for j in range(n) if (i & (1 << j)) != 0)
        if subset_sum == 0:
            subset_sum0_value = True

        print()
        print(f'j:                {list(j for j in range(n))}')
        print(f'(1 << j):         {list(bin(1 << j) for j in range(n))} << Returns 1 ({bin(1)}) with the bits shifted to the left by j places (and new bits on the right-hand-side are zeros)')
        print(f'i:                {[bin(i) for j in range(n)]}')
        print(f'i & (1 << j):     {[bin(i & (1 << j)) for j in range(n)]} & Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of i AND of (1<<j) is 1, otherwise it"s 0.')
        print(f'Podzbiory:        {list(numbers[j] for j in range(n))}')
        print(f'Podzbior_wybrany: {list(numbers[j] for j in range(n) if (i & (1 << j)) != 0)}   when (i & (1 << j)) != 0)')

    return subset_sum0_value

print(subset_sum0(numbers)) #O(n2^n)