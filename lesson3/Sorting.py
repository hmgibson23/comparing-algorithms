import random
import itertools
import sys
sys.path.append("..")

from heapq import merge
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

### Quicksort - http://en.wikipedia.org/wiki/Quicksort
@timing
def quickSort(n):
    res = qs(n)
    return res

# The actual quicksort algorithm
### I would highly recommend learning and understanding the quicksort
# algorithm as it is one of the fundamental ones used.
# This is a somewhat naive quicksort, which is why it's
# outperformed by the merge and heap sorts. A better
# quicksort, mostly, has no competitor.
def qs(n, pivotPoint = 0):
    less = []
    pivotList = []
    more = []
    if len(n) <= 1:
        return n
    else:
        pivot = n[pivotPoint]
        for i in n:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = qs(less)
        more = qs(more)
        return less + pivotList + more

@timing
def betterQuickSort(n):

    def bqs(n):
        less = []
        pivotList = []
        more = []
        if len(n) <= 1:
            return n
        else:
            pivot = n[len(n)/2]
            for i in n:
                if i < pivot:
                    less.append(i)
                elif i > pivot:
                    more.append(i)
                else:
                    pivotList.append(i)
            less = bqs(less)
            more = bqs(more)
            return less + pivotList + more

    return bqs(n)


### Note that heapsort is a pretty complicated algorithm
### http://en.wikipedia.org/wiki/Heapsort
# Internally, the Linux kernel uses heap sort because it is
# consistently O(n log n). It is, however not a stable sort.
@timing
def heapSort(n):
  for start in range((len(n) - 2) / 2, -1, -1):
    siftDown(n, start, len(n)-1)

  for end in range(len(n) - 1, 0, -1):
    n[end], n[0] = n[0], n[end]
    siftDown(n, 0, end - 1)
  return n

def siftDown(n, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and n[child] < n[child + 1]:
      child += 1
    if n[root] < n[child]:
      n[root], n[child] = n[child], n[root]
      root = child
    else:
      break

### A merge sort algorithm
# I cheated and used the merge from the heapq module
# because I'm lazy and couldn't be bothere to implement it
# myself.
# Merge sort is generally slower than heap sort but it is a stable sort.
@timing
def mergeSort(n):
    return ms(n)

def ms(n):
    if len(n) <= 1:
        return n

    middle = len(n) // 2
    left = n[:middle]
    right = n[middle:]

    left = ms(left)
    right = ms(right)
    return list(merge(left, right))

def main():

    values = random.sample(xrange(1000), 500)

    sorted = bubbleSort(values)

    sorted = quickSort(values)
    sorted = betterQuickSort(values)
    sorted = heapSort(values)

    sorted = mergeSort(values)

if __name__ == "__main__":
    main()
