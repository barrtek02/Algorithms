import numpy as np

def x1(n):
    if not isinstance(n, int) or n < 0:
        return 'n ∉ {1,2, . . .}'
    elif n==0:
        return 1
    return 3**n + x1(n-1)

def x1_a(n):
    if not isinstance(n, int) or n < 0:
        return 'n ∉ {1,2, . . .}'
    return int((3/2)*((3**n)-1)+1)

def check_x1(n):
    for N in range(n):
        print(f'n={N}, {x1.__name__}={x1(N)}, {x1_a.__name__}={x1_a(N)}, {x1(N)==x1_a(N)}')

# N = 10
# check_x1(N)


def x2(n):
    if not isinstance(n, int) or n < -1:
        return 'n ∉ {1,2, . . .}'
    elif n==-1 or n==0:
        return 0
    return n + x2(n-2)

def x2_a(n):
    if not isinstance(n, int) or n < 0:
        return 'n ∉ {1,2, . . .}'
    return (n//2) * ((n+2)//2) if n % 2 == 0 else ((n+1)//2) * ((n+1)//2)


def check_x2(n):
    for N in range(n):
        print(f'n={N}, {x2.__name__}={x2(N)}, {x2_a.__name__}={x2_a(N)}, {x2(N)==x2_a(N)}')

# N = 10
# check_x2(N)

def x3(n):
    if not isinstance(n, int) or n < 0:
        return 'n ∉ {2,3, . . .}'
    elif n==1:
        return 1
    elif n==0:
        return 0
    return x3(n-1) + x3(n-2)

def x3_a(n):
    if not isinstance(n, int) or n < 0:
        return 'n ∉ {2,3, . . .}'
    return int(((1/np.sqrt(5)) * (((1+np.sqrt(5))/2)**n - ((1-np.sqrt(5))/2)**n)))


def check_x3(n):
    for N in range(n):
        print(f'n={N}, {x3.__name__}={x3(N)}, {x3_a.__name__}={x3_a(N)}, {x3(N)==x3_a(N)}')

N = 10
check_x3(N)