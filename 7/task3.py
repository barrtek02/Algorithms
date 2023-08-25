import numpy as np
from task2 import fft


def ifft(y):
    """Inverse FFT"""

    y = fft([x.conjugate() for x in y])
    y = [x.conjugate()/len(y) for x in y]
    
    return y


def multiply_poly_fft(A, B):
    """Fast polynomials multiply using FFT """

    n = len(A) + len(B)
    n = 1 << (n - 1).bit_length()

    A.extend([0]*(n-len(A)))
    B.extend([0]*(n-len(B)))

    fft1 = fft(A)
    fft2 = fft(B)

    fft_product = [fft1[i] * fft2[i] for i in range(n)]

    # wykonaj odwrotną DFT, aby uzyskać wynikowy wielomian
    inverse_fft = ifft(fft_product)
    result = [round(x.real) for x in inverse_fft]  # zaokrąglij wynikowe współczynniki

    return result[:n-1]





if __name__ == '__main__':

    samples = [1, 0, 1, 0, 1, 0, 1, 0]
    harmonics = ifft(samples)
    assert np.allclose(harmonics, np.fft.ifft(samples))

    poly1 = [1, 2, 3, 4, 5]
    poly2 = [4, 5]
    print([4, 13, 22, 31, 40, 25, 0])
    result = multiply_poly_fft(poly1, poly2)
    print(result)
