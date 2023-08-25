def multiply_polynomials_naive(A, B):
    """O(n^2)"""

    if len(A)>len(B):
        n, m = len(A), len(B)
    else:
        m, n = len(A), len(B)

    result = [0] * (n+m-1)

    for k in range(2*n+1):
        for l in range(k+1):
            if l<len(A) and k-l<len(B):
                result[k] += A[l]*B[k-l]
    return result



if __name__ == '__main__':

    poly1 = [1, 2, 3, 4, 5]  #x^2 + 2x + 3
    poly2 = [4, 5]     #4x + 5

    result = multiply_polynomials_naive(poly2, poly1)
    assert result == [4, 13, 22, 31, 40, 25]
    print(result)
