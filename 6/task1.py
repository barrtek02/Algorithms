from math import sqrt

def prime_factors(n):
    factors = []
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            factors.append(i)
            factors.extend(prime_factors(n // i))
            return factors
    if not factors:
        factors.append(n)
    return factors



if __name__ == '__main__':
    print(prime_factors(67))
    print(prime_factors(5))
    print(prime_factors(68))
