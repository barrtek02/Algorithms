import numpy as np
def fft(a):
    """Fast Fourier Transform."""

    n = len(a)
    if n == 1:
        return a
    w_n = np.exp(-2j * np.pi / n)
    w = 1

    even = fft(a[0::2]) #y[0]
    odd = fft(a[1::2]) #y[1]
    y = [0] * n
    # y = np.zeros(n, dtype=np.complex128) #or y = [0] * n

    for k in range(n//2):
        y[k] = even[k] + w*odd[k]
        y[k + n//2] = even[k] - w*odd[k]
        w *= w_n
    return y



if __name__ == '__main__':
    samples = [1, 0, 1, 0, 1, 0, 1, 0]
    harmonics = fft(samples)
    print(harmonics)
    assert np.allclose(harmonics, np.fft.fft(samples))
