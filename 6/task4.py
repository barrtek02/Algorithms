from random import randint
from task2 import sera


def power_modulo(a, b, n):
    """Fast modular exponentiation involves squaring using the binary representation of the exponent."""

    b = bin(b)
    k = len(b)
    d = 1
    for i in range(k - 1, 0, -1):
        if b[i] == '1':
            d = (d * a) % n
        a = (a * a) % n

    return d


def is_prime_fermat(n, k=5):
    """
    Probabilistic test for primality using Fermat's Little Theorem.
    Returns True if n is probably prime, False if it is definitely composite.
    k is the number of iterations to perform (default is 5).
    """

    def is_pseudoprime(a, n):
        """The test is based on Fermat's theorem.
        For a prime number, it is guaranteed that a^(n-1) ≡ 1 (mod n)."""

        if power_modulo(a, n - 1, n) == 1:
            return True
        else:
            return False

    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(k):
        a = randint(1, n - 1)
        if not is_pseudoprime(a, n):
            return False
    return True


def is_prime_miller_rabin(n, k=20):
    """True if n is probably prime, False if it is definitely composite."""

    def witness(a, n):
        """The function witness(a, n) is used to check if
        the number a is a "witness" of the primality of the number n
        in the Miller-Rabin algorithm."""
        b = bin(n - 1)
        d = 1
        for i in range(len(b)):
            x = d
            d = power_modulo(d, 2, n)
            if d == 1 and x != 1 and x != n - 1:
                return True
            if b[i] == '1':
                d = power_modulo(d * a, 1, n)
        if d != 1:
            return True
        return False

    if n < 2:
        return False
    if n == 2 or n == 3:
        return True

    for i in range(k):
        a = randint(1, n - 1)
        if witness(a, n):
            return False

    return True


if __name__ == '__main__':
    assert power_modulo(7, 8, 14) == 7
    assert power_modulo(7, 7, 14) == 7
    assert power_modulo(5,11, 14)==3
    n_to_check = 100000
    prime_numbers = sera(n_to_check)
    for i in range(1, n_to_check):
        fermat = is_prime_fermat(i)
        rabin = is_prime_miller_rabin(i)
        prime_value = prime_numbers[i]
        assert fermat == rabin == (prime_value == 1)
        print(
            f'{i},  is_prime: {prime_value == 1}, is_prime_fermat: {fermat}, is_prime_miller_rabin: {rabin},    the same values: {fermat == rabin == (prime_value == 1)}')
