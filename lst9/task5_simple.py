import matplotlib.pyplot as plt
import random

def left(i):
  return 2*i + 1

def right(i):
  return 2*i + 2
def heapify(A, hs, i, ax):
    max_val = i
    l = left(i)
    r = right(i)

    if l < hs and A[l] > A[i]:
        max_val = l

    if r < hs and A[r] > A[max_val]:
        max_val = r

    if max_val != i:
        A[i], A[max_val] = A[max_val], A[i]
        ax.clear()
        ax.bar(range(len(A)), A, align='center')
        plt.pause(0.5)
        heapify(A, hs, max_val, ax)


def heapBuild(A, ax):
    hs = len(A)
    for i in range(hs // 2 - 1, -1, -1):
        heapify(A, hs, i, ax)


def heapSort(A):
    fig, ax = plt.subplots()
    ax.bar(range(len(A)), A, align='center')
    plt.pause(0.5)

    heapBuild(A, ax)
    for i in range(len(A) - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        ax.clear()
        ax.bar(range(len(A)), A, align='center')
        plt.pause(0.5)
        heapify(A, i, 0, ax)


def partition(A, l, u, ax):
    x = A[u]
    i = l - 1
    for j in range(l, u):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
            ax.clear()
            ax.bar(range(len(A)), A, align='center')
            plt.pause(0.5)

    if i < u:
        A[i+1], A[u] = A[u], A[i+1]
        ax.clear()
        ax.bar(range(len(A)), A, align='center')
        plt.pause(0.5)
        return i + 1
    else:
        return i


def quickSort(A, l=0, u=None, ax=None):
    if u is None:
        u = len(A) - 1

    if l < u:
        part = partition(A, l, u, ax)
        quickSort(A, l, part - 1, ax)
        quickSort(A, part + 1, u, ax)


# Przykładowe dane wejściowe
A = random.sample(range(1, 101), 10)

# Sortowanie przez kopcowanie
heapSort(A.copy())

# Sortowanie szybkie
fig, ax = plt.subplots()
ax.bar(range(len(A)), A, align='center')
plt.pause(0.1)
quickSort(A, ax=ax)

plt.show()
