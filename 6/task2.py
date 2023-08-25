from math import sqrt

def sera(p): #prime numbers
    """Generates list of 0 and 1 len p with 1 if number is prime"""
    x = [1 for i in range(p+1)]
    x[0] = x[1] = 0
    for n in range(2, int(sqrt(p))+1):
        if x[n] == 1:
            for j in range(2, p//n+1):
                x[n*j] = 0
    return x

if __name__ == '__main__':
    p = 6
    primes = (sera(p))
    print('Numbers: ', [i for i in range(p+1)])
    print('Primes:  ', primes)
    l = 0
    primes_int = []
    for i in primes:
        if i ==1:
            primes_int.append(l)
        l+=1
    print(primes_int)

