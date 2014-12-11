import itertools
import sys
sys.path.append("..")
from helpers.Helpers import *


@timing
def bubbleSort(n):
    for i in reversed(range(len(n))):
        finished = True
        for j in range(i):
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
                finished = False
        if finished:
            break
    return n

@timing
def mergeSort(n):
    return n

@timing
def quickSort(n):
    res = qs(n)
    return res

# The actual quicksort algorithm
def qs(n):
    less = []
    pivotList = []
    more = []
    if len(n) <= 1:
        return n
    else:
        pivot = n[0]
        for i in n:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more


def main():
    values = [range(100, 50), range(23,28)] + [range(3, 10), range(200, 54)]
    values = list(itertools.chain.from_iterable(values))

    sorted = bubbleSort(values)
    print "Bubble sort result: " + str(sorted)

    sorted = quickSort(values)
    print "Quick sort result: " + str(sorted)

if __name__ == "__main__":
    main()
