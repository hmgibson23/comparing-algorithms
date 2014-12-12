import random
import itertools
import sys
sys.path.append("..")
from helpers.Helpers import *
from lesson3.Sorting import *

# Remember the naive quicksort from last week that didn't do as well as the others?
# It can be improved by chossing a random pivot instead of our very naive first
# attempts i.e make the pivot the first element in the array.
# Now the quicksort has consistent O(n log n) running time and dominates almost
# every other sorting algorithm.

# BTW, quicksort can be optimised even more (make it iterative etc.) so it's so
# fast it will make your eyes bleed. The version below, however illustrates my point
# nicely enough. See http://www.csie.ntu.edu.tw/~b93076/p847-sedgewick.pdf for more.

@timing
def qsort2(n):
    return qsort(n)

def qsort(n):
    if len(n)<2: return n
    pivot_element = random.choice(n)

    # In Python QuickSort will be much faster with list comprehensions
    small = [i for i in n if i < pivot_element]
    medium = [i for i in n if i == pivot_element]
    large = [i for i in n if i > pivot_element]
    return qsort(small) + medium + qsort(large)

def main():

    values = random.sample(xrange(5000), 5000)

    sorted = bubbleSort(values)

    sorted = heapSort(values)

    sorted = mergeSort(values)

    sorted = qsort2(values)

if __name__ == "__main__":
    main()
